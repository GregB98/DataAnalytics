#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:56:56 2021

@author: greg
"""

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

import requests

url = "https://en.wikipedia.org/wiki/Rovaniemi"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Finding the nicknames
Nickname = soup.find('div', class_='nickname').text

#Finding coordinates
lat = soup.find('span' , class_='latitude').text
long = soup.find('span' , class_='longitude').text

#Finding Rovaniemi's population
everything = soup.find(class_='infobox geography vcard')

print(everything.prettify())
popstring = ""
btes= everything.find_all('td',class_='infobox-data')
for i in btes:
    tr = i.find('tr',class_="mergedrow")
    if i.string == "63,556":
        popstring = i.string
    print (i.text.strip())
    
print ("the population of Rovaniemi " + popstring)
    

url = "https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


data = pd.read_html(url)
actual_data = data[0]

actual_data.rename(columns={'Country':'Country',
                            'Average yearly temperature (1961–1990, degrees Celsius)':'avg_temp',
                            }, inplace=True)
print(actual_data.head())