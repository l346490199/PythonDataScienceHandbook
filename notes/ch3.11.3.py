#!/bin/python3
#-*- coding: utf-8 -*-
# ch3.11.3.py
# @author 刘秋
# @email lq@aqiu.info
# @description 
# @created 2020-08-13T11:37:29.278Z+08:00
# @last-modified 2020-08-13T11:42:23.749Z+08:00
#

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

path = r"notebooks\data\recipeitems-latest.json"
try:
    recipes=pd.read_json(path)
except ValueError as e:
    print('ValueError',e)