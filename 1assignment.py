#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:15:33 2021

@author: greg
"""
import numpy as np

ListOfOne = []
ListOfSeven = []
ListOfFifty =[]
ListOfEven = []
ListOfYears = []
# These are the regular Python arrays
for i in range (15):
    ListOfOne.append(1)
    
print ("All Ones" , ListOfOne)   

for i in range(15):
    ListOfSeven.append(7)
    
print ("All sevens" ,  ListOfSeven)    
    
 
for i in range(100,151):
    ListOfFifty.append(i)
        
print ("List from 100 to 150" ,  ListOfFifty)  

for i in range(0,101):
    if i % 2 == 0:
        ListOfEven.append(i)
print ("\n")
print ("List of even numbers" , ListOfEven)    

for i in range(1950,2021):
    if i % 4 == 0:
        ListOfYears.append(i)

print ("\n")
print ("List of years" , ListOfYears)

        # These are the Numpy Arrays
Zeroes = np.zeros(15)
Ones = np.ones(15)

Sevens = np.repeat(7,15)
print ("\n")
print ("Np sevens" , Sevens)
print ("\n")

Hundred = np.arange(100,151)
print ("\n")
print ("Np hundred" , Hundred)
print ("\n")
NineTeenHundred = np.arange(1900,2021)

Even = np.arange(0,101,2)
print ("\n")
print ("Np even" , Even)


DivByFour = np.arange(1950,2023,4)
print ("\n")
print("Np Divbyfour", DivByFour)
print ("\n")

        #These are the Numpy Matrixes
        
MatrixOfFortyNine = np.arange(1,50).reshape(7,7)
print ("\n")
print ("\n")
print(MatrixOfFortyNine)

MatrixOfRandom = np.random.randint(1,6,64).reshape(8,8)
print ("\n")
print ("\n")
print(MatrixOfRandom)

MatrixOfLin = np.linspace(-3,4,64).reshape(8,8)
print ("\n")
print ("\n")
print(MatrixOfLin)

MatrixOfLinTen = np.linspace(0,2,10)
print ("\n")
print ("\n")
MatrixOfFive =np.linspace(0,6,100).reshape(10,10)

#These are the matrixes of Task Five
print ("\n")
print ("\n")
TaskfiveFirst = np.array([23,34,54,34,56,33,56,78,65,78,41,32,11,34,56])
TaskfiveFirst = TaskfiveFirst.reshape(5,3)

print(TaskfiveFirst)
print ("\n")
print ("\n")

TaskfiveSec = np.arange(128,256).reshape(8,16)
print(TaskfiveSec)
print ("\n")
print ("\n")
TaskfiveThird = np.arange(0.05,5.05,0.05).reshape(10,10)
print(TaskfiveThird)

print ("\n")
print ("\n")
#These are the matrixes of Task Six

dataset = np.arange(1,37).reshape(6,6)
MatrixSlice = dataset[3:,2:]
print(MatrixSlice)
print ("\n")
print ("\n")
Column = dataset[:4,3]
print(Column)
print ("\n")
print ("\n")
Row = dataset[2]
print (Row)
print("\n")
print ("\n")
MatrixSliceTwo = dataset[3:,0:]
print(MatrixSliceTwo)


#Excercise Six Operations

SumOfAll = np.sum(dataset)
print (SumOfAll)
print ("\n")
SumOfOdd =np.sum(dataset[dataset%2==1])
print(SumOfOdd)
print ("\n")
Standard = np.std(dataset)
print(Standard)
print ("\n")
SumByColumn = dataset.sum(axis=0)
print (SumByColumn)
print ("\n")
SumByRow = dataset.sum(axis=1)
print (SumByRow)




