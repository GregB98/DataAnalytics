#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 12:51:33 2021

@author: greg
"""
import datetime as dt
import pandas as pd

data= pd.read_csv('purchases.csv')
#Sum of the Purchases of buyer 018H2015
PurchaseByID = data[data['Purchase Order Number'] == "018H2015"]
PurchaseByID = PurchaseByID['Total Price'].sum()

#Description of Purchase item 3176273
PurchaseByOrder = data[data['Purchase Order Number'] == "3176273"]
PurchaseByOrder = PurchaseByOrder[['Item Name','Item Description']]
# orders in 2013
PurchaseByYear = data[data['Purchase Date'].str.contains('2013')]
#By department name
helper = 5
MostCommonDepartment = data['Department Name'].value_counts()[:helper].index.tolist()

SortByDepartment= data.sort_values('Department Name')