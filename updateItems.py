# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:11:59 2019

@author: pratprak
"""

import pandas as pd

FILE_PATH = 'C:\Users\pratprak\Documents\itemData\items.csv'

df = pd.read_csv(FILE_PATH) 

print(df.head())

#Update item
def updateItems(item_id):
    item = df.loc[df['item_id']  == item_id]
    item_sold_count = item['item_sold'].astype('int').values
    print(item_sold_count)
    inital_count = item_sold_count[0]
    incr_count = inital_count + 1
    item_index = df.index[df['item_id']  == item_id]
    df.set_value(item_index, "item_sold", incr_count)
    df.reset_index()
    print(df.head())

#Save Data To ./csv
def saveData():
    df.to_csv(FILE_PATH, index=False)

updateItems(11)
    
saveData()