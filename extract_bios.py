# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:04:19 2017

@author: w9641432
"""

#%%
def extract_bios(sheet,name):
    
    namn=[]
    Fname=[]
    Lname=[]
    Tarm=[]
    battst=[]
    Nation=[]
    for rowOfCellObjects in sheet['A2':'A19106']: # Data from 2014-2016,cell number 
            for cellObj in rowOfCellObjects:
                namn.append(cellObj.value)
    for rowOfCellObjects in sheet['E2':'E19106']: # Data from 2014-2016,cell number 
            for cellObj in rowOfCellObjects:
                Nation.append(cellObj.value)
    for rowOfCellObjects in sheet['N2':'N19106']: # Data from 2014-2016,cell number 
            for cellObj in rowOfCellObjects:
                Fname.append(cellObj.value)
    for rowOfCellObjects in sheet['O2':'O19106']: # Data from 2014-2016,cell number 
            for cellObj in rowOfCellObjects:
                Lname.append(cellObj.value)
    for rowOfCellObjects in sheet['T2':'T19106']: # Data from 2014-2016,cell number 
            for cellObj in rowOfCellObjects:
                Tarm.append(cellObj.value)
    for rowOfCellObjects in sheet['S2':'S19106']: # Data from 2014-2016,cell number 
            for cellObj in rowOfCellObjects:
                battst.append(cellObj.value)
                
    
    
    for k in range(0,len(namn)):
        if name in namn[k]:
            Firstname=Fname[k]
            Lastname=Lname[k]
            ThrowA=Tarm[k]
            Batstance=battst[k]
            Nationality=Nation[k];

    
    bios = [Firstname,Lastname,Nationality,ThrowA,Batstance]
    return bios


