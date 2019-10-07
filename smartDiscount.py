# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:27:10 2019

@author: pratprak
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits import mplot3d

style.use("ggplot")
from sklearn import linear_model

FILE_PATH = "C:\Users\pratprak\Documents\itemData\discountTrends.csv"

data = pd.read_csv(FILE_PATH, sep="\t")

print(data.head())

X = data[['item_id','subitem_id']]
y = data['discount'].astype('float').values

#Generates Dynamic discounts on Items combined with a Subitem
def getDiscount(item_id,subItem_id):
    clf = linear_model.SGDRegressor(max_iter = 100,tol= 1e-3)
    clf.fit(X, y)
    X_test = np.array([[item_id, subItem_id]])
    y_test = clf.predict(X_test)
    return y_test
   
#Generates a graph plot of discount distribution    
def getDiscountPlot():
    ax = plt.axes(projection='3d')
    x1 = data['item_id'].astype('float').values
    y1 = data['subitem_id'].astype('float').values
    z1 = data['discount'].astype('float').values
    
    ax.bar3d(x1, y1, z1, 0.5, 0.5, 10, color='aqua')
    ax.set_xlabel('Items')
    ax.set_ylabel('SubItems')
    ax.set_zlabel('Discounts')
    plt.show()

y_test = getDiscount(1, 24)

print(y_test)

getDiscountPlot()