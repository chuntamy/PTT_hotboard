#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 00:23:19 2024

@author: chuntamy
"""

import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup

def get_articles(url):
    
    response = requests.get(url, "html.parser", cookies={'over18': '1'})
    response.encoding = "UTF-8"
    soup = BeautifulSoup(response.text, 'html.parser')
    
    hotboards = []
    for board_div in soup.find_all('div', class_='b-ent'):
        board_details = {}
        
        board_details['name'] = board_div.find('div', class_='board-name').text
        board_details['popularity'] = board_div.find('div', class_='board-nuser').text
        board_details['category'] = board_div.find('div', class_='board-class').text
        board_details['title'] = board_div.find('div', class_='board-title').text
        board_details['link'] = 'https://www.ptt.cc/'+ board_div.find('a').get("href")

        hotboards.append(board_details)
    return pd.DataFrame(hotboards)[['name', 'popularity', 'title', 'category','link' ]]

hotboards = get_articles('https://www.ptt.cc/bbs/index.html')
hotboards.to_csv('hotboards.csv', encoding='utf-8')