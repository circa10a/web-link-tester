#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests, sys

def check_protocol(site): #Validate argument starts with http or https
    return site.startswith('http://') or site.startswith('https://')

def create_json(response, link):
    data = {}
    data['code'] = response
    data['url'] = link
    return data

def test_links(site):
    try:
        r  = requests.get(site)
        soup = BeautifulSoup(r.text, 'html.parser')
        json_data=[]
        for link in soup.find_all('a'):
            link = str(link.get('href'))
            link = link.replace("'",'"')
            if check_protocol(link):
                response = requests.get(link)
                key_pair = create_json(response.status_code,link)
                json_data.append(key_pair)
        return json_data
    except requests.ConnectionError:
        return ('Unable to Connect')
    except requests.exceptions.MissingSchema:
        return ('Error. Please Use Full URL (e.g "https://google.com")')
    except:
        return ('Unknown error has occurred')
