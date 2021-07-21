#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:36:51 2021

@author: greg
"""
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


data= pd.read_csv('mpg.csv')
#Converting MPG to l/100km and dropping columns
data['Liters_per_100_km'] = (100*3.785411784/(1.609344*data['mpg']))
data= data.drop('name',axis=1)
data=data.drop('mpg',axis=1)
#Correlations
Correlations = data.corr()

#dropping colums which don't corelate
data=data.drop('acceleration',axis=1)
data=data.drop('model_year',axis=1)

#I dropped the cylinders column 
#because it has the lowest corelation values 
#of all of the listed three


data=data.drop('cylinders',axis=1)

#Pairplotting for consumption
sns.pairplot(data,hue='origin')
#cars from the USA have more overall petrol consumtion
#cars from Europe have the lowest consumption
#thes cars also have smaller displacement,horsepower and weight