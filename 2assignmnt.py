#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 09:39:31 2021

@author: greg
"""

import pandas as pd

data= pd.read_csv('loans.csv')

print(data.head())
# Selecting then dropping too big loans
SelectTooBigLoan =data[ data['Current Loan Amount'] > 99999999 ].index
data.drop(SelectTooBigLoan , inplace=True)

#Filtering out NaN values
data = data.dropna()

print(data.head())

#Average of Current Loan
 
AvgLoan = data['Current Loan Amount'].mean()

#Min and Max values of the annual incomes
MinIncome = data['Annual Income'].min()
MaxIncome = data['Annual Income'].max()

#Home Ownership status and Annual Income value of these rows

HomeOwnerShip = data[data['Loan ID'] == "bbf87a87-22cd-4d10-bd9b-7a9cc1b6e59d"]
HomeOwnerShip = HomeOwnerShip['Home Ownership']

#Calculating the Actual Income of the user
AnnualIncome = data[data['Loan ID'] == "76fa89b9-e6a8-49af-afa1-8151315aba8e"]     
Debt = AnnualIncome['Monthly Debt']
AnnualIncome = AnnualIncome['Annual Income']                  
ActualIncome = AnnualIncome-(12* Debt)

#Finding the Loan ID of the smallest Annual Income
SmallestIncome = data.loc[data['Annual Income'].idxmin()]['Loan ID'] 

#Counting the Long Term loans

LongTerm = data[data['Term'].str.find('Long') >= 0]

#Counting more than one Bankruptcy

Bankruptcy = data[data['Bankruptcies'] > 1].count()

#Short Term and for House Improvement
ShortHouse = data[data['Term'].str.find('Short') >= 0]
ShortHouse = ShortHouse[ShortHouse['Purpose'].str.find('Home') >= 0].count()

#Unique purposes

UniLoan = data['Purpose'].unique()
helper = 3
Mostcommon = data['Purpose'].value_counts()[:helper].index.tolist()

#Correlations


data['Annual Income'] = data['Annual Income'].astype('float')
data['Number of Open Accounts'] = data ['Number of Open Accounts'].astype('float')
IncomeOpenAccounts = data['Annual Income'].corr(data['Number of Open Accounts'])


data['Number of Credit Problems'] = data['Number of Credit Problems'].astype('float')
data['Bankruptcies'] = data['Bankruptcies'].astype('float')
CreditProblemsBankruptcies = data['Bankruptcies'].corr(data['Number of Credit Problems'])



# Second Excercies























