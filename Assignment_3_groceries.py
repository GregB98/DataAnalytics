#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 14:13:47 2021

@author: greg
"""
import calendar
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


food = pd.read_csv('groceries.csv')

food['Fish'].fillna((food['Fish'].mean()),inplace = True)
food['Pork'].fillna((food['Pork'].mean()),inplace = True)
food['Sunflower-oil'].fillna((food['Sunflower-oil'].mean()),inplace = True)


Correlations = food.corr()
#Sunflower-oil does not follow any other trends
#Corn,Barley,Wheat and Rice have quite high correlation
#Palm oil also correlates except for Sunflower oil,Beef,Pork,Chicken,Fish,Tea and coffee


