#!/bin/python3
#-*- coding: utf-8 -*-

import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns 
from pandas_datareader import data

sns.set()
path = r"FremontBridge copy.csv"
# # data = pd.read_csv(r"FremontBridge.csv",index_col=0,skipfooter=1)
# data.index = pd.to_datetime(data.index)
# # data = data ['2012']
# print(data.index)
# data.to_csv("FremontBridge.csv")


# path = r"FremontBridge.csv"
# data = pd.read_csv(path,index_col=0)
# data.index = pd.to_datetime(data.index)
data = pd.read_csv(path,index_col='Date',parse_dates=True,skipfooter=1)
data.columns = ['Total',"East","West"]

#### 1
data.plot()
plt.ylabel('Hourly Bicycle Count')
####

###### 2
weekly = data.resample("W").sum()
weekly.plot(style=[':','--','-'])
plt.ylabel("Weekly bicycle count")
######

print(data.head())
print(data.dropna().describe())
plt.show()
