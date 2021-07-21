#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 10:45:14 2021

@author: greg
"""
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

penguins = (sns.load_dataset('penguins'))
data= pd.read_csv('penguins.csv')


# 1st excercise
Firstplot = sns.pairplot(penguins)
Correlation =penguins.corr()

plt.clf()


Islandplot = sns.pairplot(penguins, hue='island')
plt.figure()

#Number of penguins / species and / island
Value = data['island'].value_counts()
valuetwo = data['species'].value_counts()

#second pairplot
plt.clf()
Speciesplot = sns.pairplot(penguins, hue='species')
plt.figure()

#Bill to flipper
plt.clf()
sns.scatterplot(x='bill_length_mm', y = 'flipper_length_mm', data=penguins, hue='species')
plt.figure()

plt.clf()
sns.scatterplot(x='bill_length_mm', y = 'flipper_length_mm', data=penguins, hue='island')
plt.figure()

#Violinplots
plt.clf()
sns.violinplot(x='species', y='flipper_length_mm', data=penguins, hue='island')
plt.figure()

plt.clf()
sns.violinplot(x='species', y='bill_length_mm', data=penguins, hue='island')
plt.figure()

plt.clf()
sns.violinplot(x='species', y='body_mass_g', data=penguins, hue='island')
plt.figure()

