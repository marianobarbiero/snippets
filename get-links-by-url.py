#!/usr/bin/env python

import requests
import re
from urlparse import urljoin

URL=""

def process(url):
    
    req = requests.get(url)

    if(req.status_code == 200):
                
        # Finding links
        links = link_regex.findall(req.text)
        print ("\nLINKS: " + str(len(links)))
        
        for link in links:
            link = urljoin(url, link)
            print(link)
    else:
        
        print("url: " +url + " fail")
        return []        

if __name__ == '__main__':
    
    # links regex
    link_regex = re.compile(r'href="(.*?)"')

    process(URL)
    
