# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 21:45:31 2021

@author: affan
"""

import h5py
import numpy as np

def dataLoader(filename):
    
    f = h5py.File("data_training.h5", 'w')

    file=open(filename)

    data=np.loadtxt(file)

    dataNum=int(data[0][0])
    points=int(data[0][1])

    dataSet=np.zeros([dataNum,points,3])
    dataLabel=np.empty([dataNum,points], dtype='int')

    for i in range(dataNum):
       for j in range(points):
            dataLabel[i][j]=data[j][3]
            for k in range(3):
                    dataSet[i][j][k]=data[j][k]
    
    data = f.create_dataset("data", data = dataSet)
    label = f.create_dataset("label", data = dataLabel)

    f.close()
    file.close()
    
    return (dataSet,dataLabel)