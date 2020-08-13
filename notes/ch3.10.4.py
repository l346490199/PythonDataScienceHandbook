#!/bin/python3
#-*- coding: utf-8 -*-
# ch3.10.4.py
# @author 刘秋
# @email lq@aqiu.info
# @description 美国人的生日  153页
# @created 2020-08-13T08:16:18.688Z+08:00
# @last-modified 2020-08-13T10:52:46.505Z+08:00
#

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = r"notebooks\data\births.csv"
births = pd.read_csv(path)
# print(births.head())
births["decade"] = 10 * (births["year"] // 10)
_print = births.pivot_table("births",
                            index="decade",
                            columns="gender",
                            aggfunc="sum")
# print(_print)
sns.set()
fig, ax = plt.subplots(figsize=(20,8),dpi=80)


# births.pivot_table('births', index='year', columns='gender',
#                    aggfunc='sum').plot()
# plt.ylabel('total births per year')

# _print = births['day']

quartiles = np.percentile(births['births'], [25, 50, 75])
mu = quartiles[1]
sig = 0.74 * (quartiles[2] - quartiles[0])

births = births.query('(births > @mu - 5*@sig)&(births < @mu +5 *@sig)')

births['day'] = births['day'].astype(int)

births.index = pd.PeriodIndex(year=births.year,month=births.month,day=births.day,freq='D')
births['dayofweek'] = births.index.dayofweek

births.pivot_table('births',index='dayofweek',columns='decade',aggfunc='mean').plot(ax=ax)
ax.set_xticks(range(0,7))
ax.set_xticklabels(['Mon','Tues','Wed','Thurs','Fri','Sat','Sun'])
ax.set_ylabel('mean births by day')


births_by_date = births.pivot_table('births',[births.index.month,births.index.day])

births_by_date.index=[pd.datetime(2020,month,day) for (month,day) in births_by_date.index]


# 绘制平均每日的出生人数
Fig,Axes=plt.subplots(figsize=(12,4))
births_by_date.plot(ax=Axes)

# 图像标签
plt.xlabel('Date')
plt.ylabel('Number')
plt.title('Number of Birth Per Day')


_print = births_by_date.head()
print(_print)
plt.show()
