#!/bin/python3
#-*- coding: utf-8 -*-
# ch3.12.5.py
# @author 刘秋
# @email lq@aqiu.info
# @description 
# @created 2020-08-17T09:09:03.785Z+08:00
# @last-modified 2020-08-17T11:15:17.332Z+08:00
#

import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns 
from pandas_datareader import data

sns.set()

# goog = data.DataReader('GOOG',start='2004',end='2016',data_source='yahoo')
# goog.to_csv("./123.csv")
goog = pd.read_csv('./123.csv',index_col=0)
goog.index = pd.to_datetime(goog.index)
# print(goog.index)
goog = goog["Close"]


goog.plot(alpha=0.5,style='-')
goog.resample('BA').mean().plot(style=':')
goog.asfreq('BA').plot(style='--')
plt.legend(['input','resample','asfreq'],loc='upper left')
# plt.xlabels(['2006','2007','2006','2009','2010','2011'])

############  2
fig,ax = plt.subplots(3,sharey=True,figsize=(20,8),dpi=80)
goog = goog.asfreq('D',method='pad')
goog.plot(ax=ax[0])
goog.shift(900).plot(ax=ax[1])
goog.tshift(900).plot(ax=ax[2])

local_max = pd.to_datetime('2007-11-05')
offset = pd.Timedelta(900,'D')

# 图例和标签
ax[0].legend(['input'],loc = 2)
ax[0].get_xticklabels()[4].set(weight='heavy',color='red')
ax[0].axvline(local_max,alpha=0.3,color='red')

ax[1].legend(['shift(900)'],loc = 2)
ax[1].get_xticklabels()[4].set(weight='heavy',color='red')
ax[1].axvline(local_max+offset,alpha=0.3,color='red')

ax[2].legend(['tshift(900)'],loc = 2)
ax[2].get_xticklabels()[1].set(weight='heavy',color='red')
ax[2].axvline(local_max+offset,alpha=0.3,color='red')
############

################  3
ROI = 100*(goog.tshift(-365)/goog -1)
FIG, AX = plt.subplots(figsize=(20,8),dpi=80)
ROI.plot(ax=AX)
AX.set_ylabel('% Return on Investment')
AX.axvline(0,alpha=0.3,color='red')
################

#################  4
rolling = goog.rolling(365,center=True)
data  = pd.DataFrame({"input":goog,'one-year rolling_mean':rolling.mean(),"one-year rolling_std":rolling.std()})
ax = data.plot(style=['-','--',':'])
ax.lines[0].set_alpha(0.3)
#################
plt.show()
# _print = goog.head()

# print(_print)

