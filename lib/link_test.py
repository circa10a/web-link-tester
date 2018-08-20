from bs4 import BeautifulSoup
from flask import jsonify
from requests_futures.sessions import FuturesSession
import requests, sys, os

num_workers = os.cpu_count()
session = FuturesSession(max_workers=num_workers)

def checkProtocol(url): #Validate argument starts with http or https
    return url.startswith('http://') or url.startswith('https://')

def createJson(response, link):
    data = {}
    data['code'] = response
    data['url'] = link
    return data

def linkCheck(url):
    try:
        r  = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        jsonData = []
        urls = []
        futures = []
        for link in soup.find_all('a'):
            link = str(link.get('href'))
            link = link.replace("'",'"')
            if checkProtocol(link):
                urls.append(link)
                futures.append(session.get(urls.pop(0)))
        for future in futures:
            response = future.result()
            keyPair = createJson(response.status_code, response.url)
            jsonData.append(keyPair)
        return jsonData
    except requests.ConnectionError:
        return jsonify({'error': 'unable to connect'})
    except requests.exceptions.MissingSchema:
        return jsonify({'error': 'missing http://'})
    except(Exception) as e:
        print(e)
        return jsonify({'error': 'unknown'})
