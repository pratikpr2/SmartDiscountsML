# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:45:19 2019

@author: pratprak
"""

import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

FILE_PATH = 'C:\Users\pratprak\Documents\itemData\items.csv'

df = pd.read_csv(FILE_PATH)
print(df.head(5))
print('\n')

#Gets Sales Graph In The Restaurant
def getSalesGraph():                        
    plt.bar(df['item_name'],df['item_sold'], color=(0.5,0.1,0.5,0.6))
    plt.xticks(df['item_name'], rotation=90)
    plt.show()
    
#Gets Popular Items In The Restaurant
def getPopItems():                          
        print('----------Most Popular In your Restaurant-----------------')
        burger_pop = df.loc[df['item_type'] == 'burger']
        burger_pop = burger_pop.sort_values(['item_sold','item_price'], ascending=False)
        print(burger_pop)
        item_array = burger_pop['item_id'].to_numpy()
        return item_array  
    
#Gets Least Popular Items In the Restaurant   
def getSubItems():
    print('------------------ On Offers ------------------------------')
    offer_items = df.loc[df['item_type'] != 'burger']
    offer_items = offer_items.sort_values(['item_price', 'item_sold'], ascending = True)
    print(offer_items.head())
    offer_items_arr = offer_items['item_id'].to_numpy()
    return offer_items_arr

getSalesGraph()

pop_item_array = getPopItems()
print(pop_item_array)

offer_item_array = getSubItems()
print(offer_item_array)  

















