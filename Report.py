#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:55:28 2021

@author: greg
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#I will drop any values which occured after 2016 because there are not many values

df= pd.read_csv('vgsales.csv')
df = df.drop(df[df.Year >= 2016].index)

#I will drop the name column
#And drop any rows with NaN values
#There were several in the year and sales columns

df= df.drop('Name',axis=1)
df.dropna(inplace=True)

#total sales of videogames 
totdf = df.filter(['Year','Genre','Global_Sales'], axis=1)

SaleByYear= totdf.groupby(['Year'])['Global_Sales'].sum()
SaleByYear = SaleByYear.reset_index(level=['Year'])
#with this we can see the "Great Video Game Crash of 1983 " 
#and that sales have doubled in 1996 which corresponds 
#to the release date of the N64 and Playstation consoles

plt.clf()
yearplot = sns.barplot(x="Year",y="Global_Sales",data=SaleByYear,)
yearplot.set_xticklabels(yearplot.get_xticklabels(), rotation=40, ha="right")
yearplot.set_xticklabels(yearplot.get_xticklabels(), fontsize=8)
plt.tight_layout()
plt.figure(figsize=(16,4))

#Which was the most popular genre of game by year and how much did they sell
worker = totdf.groupby(['Year','Genre'])['Global_Sales'].sum()
GenreByYear = worker.loc[worker.groupby(level=0).idxmax()]
GenreByYear = GenreByYear.reset_index(level=['Year','Genre'])
plt.clf()
genplot = sns.barplot(x="Year",y="Global_Sales",data=GenreByYear,hue="Genre",dodge=False)
genplot.set_xticklabels(genplot.get_xticklabels(), fontsize=7)
genplot.set_xticklabels(genplot.get_xticklabels(), rotation=40, ha="right")

plt.figure(figsize=(16,16))




#2 Platform / sale region 
platfilter = df.filter(['Platform','Genre','NA_Sales','JP_Sales','EU_Sales'])



platdf= platfilter.groupby(['Platform'])['NA_Sales', 'JP_Sales', 'EU_Sales'].sum().reset_index()

gendf = platfilter.groupby(['Genre'])['NA_Sales', 'JP_Sales', 'EU_Sales'].sum().reset_index()

#Biggest selling genre of game / year
