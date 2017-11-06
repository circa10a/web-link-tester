#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests, sys

def check_protocol(site): #Validate argument starts with http or https
    return site.startswith('http://') or site.startswith('https://')

def print_response(response, link):
    data = {}
    data["url"] = link
    data["code"] = response
    return data

def test_links(site):
    try:
        r  = requests.get(site)
    except requests.ConnectionError:
        return ('Unable to Connect')
        sys.exit(1)
    soup = BeautifulSoup(r.text, 'html.parser')
    link_list=[]
    for link in soup.find_all('a'):
        link = str(link.get('href'))
        link = link.replace("'",'"')
        if check_protocol(link):
            response = requests.get(link)
            link_list.append(print_response(response.status_code,link))
        else
        return "Error. Please Use Full URL (e.g \"https://google.com\")"
    return link_list
