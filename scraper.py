#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.offline as pyo

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager


# In[24]:


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://baseballsavant.mlb.com/leaderboard/percentile-rankings?type=pitcher&team=')
driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div[2]/form/div[2]/div/select').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div[2]/form/div[2]/div/select/option[31]').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div[2]/form/div[4]/button').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div[2]/form/div[4]/button').click()
df = pd.read_html(driver.find_element(By.ID, 'prLeaderboard').get_attribute('outerHTML'))
df = df[0]
df = df.set_index('Player')
df


# In[26]:


categories = ['xwOBA', 'HardHit%', 'K%', 'Whiff%', 'BB%']
categories = [*categories, categories[0]]

cole = [df.at['Gerrit Cole','xwOBA'], df.at['Gerrit Cole','HardHit%'],df.at['Gerrit Cole','K%'], 
        df.at['Gerrit Cole','Whiff%'], df.at['Gerrit Cole','BB%']]
sevy = [df.at['Luis Severino','xwOBA'], df.at['Luis Severino','HardHit%'],df.at['Luis Severino','K%'], 
        df.at['Luis Severino','Whiff%'], df.at['Luis Severino','BB%']]
cortes = [df.at['Nestor Cortes','xwOBA'], df.at['Nestor Cortes','HardHit%'],df.at['Nestor Cortes','K%'], 
        df.at['Nestor Cortes','Whiff%'], df.at['Nestor Cortes','BB%']]
taillon = [df.at['Jameson Taillon','xwOBA'], df.at['Jameson Taillon','HardHit%'],df.at['Jameson Taillon','K%'], 
        df.at['Jameson Taillon','Whiff%'], df.at['Jameson Taillon','BB%']]
monty = [df.at['Jordan Montgomery','xwOBA'], df.at['Jordan Montgomery','HardHit%'],df.at['Jordan Montgomery','K%'], 
        df.at['Jordan Montgomery','Whiff%'], df.at['Jordan Montgomery','BB%']]

cole = [*cole, cole[0]]
sevy = [*sevy, sevy[0]]
cortes = [*cortes, cortes[0]]
taillon = [*taillon, taillon[0]]
monty = [*monty, monty[0]]


fig = go.Figure(
    data=[
        go.Scatterpolar(r=cole, theta=categories, fill='toself', name='Gerrit Cole'),
        go.Scatterpolar(r=sevy, theta=categories, fill='toself', name='Luis Severino'),
        go.Scatterpolar(r=cortes, theta=categories, fill='toself', name='Nestor Cortes'),
        go.Scatterpolar(r=taillon, theta=categories, fill='toself', name='Jameson Taillon'),
        go.Scatterpolar(r=monty, theta=categories, fill='toself', name='Jordan Montgomery')
    ],
    layout=go.Layout(
        title=go.layout.Title(text='Yankees Starting Pitcher Percentile Rankings (2022)'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)

fig


# In[ ]:


fig.write_image("radar.svg")


# # categories = ['xwOBA', 'HardHit%', 'K%', 'Whiff%', 'BB%']
# categories = [*categories, categories[0]]
# 
# cole = [81, 34, 92, 92, 63]
# sevy = [81, 32, 78, 72, 58]
# cortes = [89, 62, 72, 39, 83]
# taillon = [44, 61, 32, 30, 98]
# monty = [37, 70, 35, 74, 92]
# 
# cole = [*cole, cole[0]]
# sevy = [*sevy, sevy[0]]
# cortes = [*cortes, cortes[0]]
# taillon = [*taillon, taillon[0]]
# monty = [*monty, monty[0]]
# 
# 
# fig = go.Figure(
#     data=[
#         go.Scatterpolar(r=cole, theta=categories, fill='toself', name='Gerrit Cole'),
#         go.Scatterpolar(r=sevy, theta=categories, fill='toself', name='Luis Severino'),
#         go.Scatterpolar(r=cortes, theta=categories, fill='toself', name='Nestor Cortes'),
#         go.Scatterpolar(r=taillon, theta=categories, fill='toself', name='Jameson Taillon'),
#         go.Scatterpolar(r=monty, theta=categories, fill='toself', name='Jordan Montgomery')
#     ],
#     layout=go.Layout(
#         title=go.layout.Title(text='Yankees Starting Pitcher Percentile Rankings (2022)'),
#         polar={'radialaxis': {'visible': True}},
#         showlegend=True
#     )
# )
# 
# pyo.plot(fig)

# In[ ]:


df.to_csv('nyy-pitch-percentile', index=False)


# In[ ]:




