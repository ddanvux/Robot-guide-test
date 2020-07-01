# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:16:28 2020

@author: Dan Vu
"""
import os
import pandas as pd
from pandas import DataFrame
os.chdir("C:/Users/Dan Vu/Desktop/")
InsFile = pd.read_csv('instruction_list.txt', sep=",", header=None, names=['Dir', 'Step'])
Universe = pd.read_csv('universe.txt', sep=":", header=None, names=['Side', 'Value'])

def leftrightscore(dataset):
    score = []
    for val in dataset.values:
        if val == 'right':
            a = 1
        else:
            a = -1
        score.append(a)
    return score
def movement(dataset):
    move =[]
    sum_ = 0
    for val in dataset:
        sum_ += val
        if sum_ < 0 or sum_>3:
            sum_= sum_%4  #sum_ modulo 4
        move.append(sum_)
    return move
def funcX(row):
    if row['Move'] == 0:
        val = 0
    elif row['Move'] == 1:
        val = row['Step']
    elif row['Move'] == 2:
        val = 0
    else:
        val = -row['Step']
    return val
def funcY(row):
    if row['Move'] == 0:
        val = row['Step']
    elif row['Move'] == 1:
        val = 0
    elif row['Move'] == 2:
        val = - row['Step']
    else:
        val = 0
    return val
def sizeuniverse(dataset):
    width = dataset['Value'].loc[0]
    height = dataset['Value'].loc[1]
    return width,height

width, height = sizeuniverse(Universe)
score = leftrightscore(InsFile['Dir'])
Move = DataFrame(movement(score),columns=['Move'])
InsFile = pd.concat([InsFile, Move],axis=1)

def getPositionFinale(dataset):
    cumX =[]
    sumX = 0
    dataX = dataset.apply(funcX, axis=1)
    for val in dataX.values:
        sumX += val
        if sumX >= width:
            sumX= width -1
        elif sumX < 0:
            sumX = 0
        else:
            sumX = sumX
        cumX.append(sumX)
    cumY =[]
    sumY = 0
    dataY = dataset.apply(funcY, axis=1)
    for val in dataY.values:
        sumY += val
        if sumY >= height:
            sumY = height -1
        elif sumY < 0:
            sumY = 0
        else:
            sumY = sumY
        cumY.append(sumY)    
    print("The object found in the spot (", cumX[-1],", ", cumY[-1],")")

getPositionFinale(InsFile)    