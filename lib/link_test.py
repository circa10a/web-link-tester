#!/usr/bin/env python
from bs4 import BeautifulSoup
from flask import jsonify
import requests, sys

def checkProtocol(url): #Validate argument starts with http or https
    return url.startswith('http://') or url.startswith('https://')

def createJson(response, link):
    data = {}
    data['code'] = response
    data['url'] = link
    return data

def test_links(url):
    try:
        r  = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        jsonData=[]
        for link in soup.find_all('a'):
            link = str(link.get('href'))
            link = link.replace("'",'"')
            if checkProtocol(link):
                response = requests.get(link)
                keyPair = createJson(response.status_code,link)
                jsonData.append(keyPair)
        return jsonData
    except requests.ConnectionError:
        return jsonify({'error': 'Unable to connect'})
    except requests.exceptions.MissingSchema:
        return jsonify({'error': 'Missing http://'})
    except:
        return jsonify({'error': 'unknown'})
