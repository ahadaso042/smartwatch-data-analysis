#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


# In[9]:


data = pd.read_csv("dailyActivity_merged.csv")
data.head()


# In[10]:


data.isnull().sum()


# In[11]:


data.info()


# In[12]:


#change the data type of the ActivityData columns
data["ActivityDate"] = pd.to_datetime(data["ActivityDate"], format="%m/%d/%Y")


# In[13]:


data.info()


# In[19]:


data["TotalMinutes"] = data["VeryActiveMinutes"] + data["FairlyActiveMinutes"] + data["LightlyActiveMinutes"] + data["SedentaryMinutes"]
data["TotalMinutes"].sample(5)


# In[20]:


data.head()


# In[21]:


data.describe()


# # Visualizations

# In[34]:


#What is the correlation between calories burned and total steps walked in a day

figure = px.scatter(data, "Calories", "TotalSteps", "TotalDistance", size = "VeryActiveMinutes", trendline = "ols", title = "Relationship Between Calories & Total Steps")
figure.show()


# In[53]:


# What is the average total number of active minutes in a day?

label = ["Very Active Minutes", "Fairly Active Minutes", "Lightly Active Minutes", "Inactive Minutes"]
counts = data[["VeryActiveMinutes", "FairlyActiveMinutes", "LightlyActiveMinutes", "SedentaryMinutes"]].mean()
colors = ["Green", "Yellow", "Orange", "Red"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Total Average Active Minutes', title_font_size = 30)
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                 marker=dict(colors=colors, line=dict(color='black', width=1)))

fig.show()


# In[54]:


data["Day"] = data["ActivityDate"].dt.day_name()
data["Day"].head()


# In[82]:


#Very Active, Fairly Active and Lightly Active minutes on each day of the week

fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["VeryActiveMinutes"],
    name='Very Active',
    marker_color = 'Purple'))

fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["FairlyActiveMinutes"],
    name='Fairly Active',
    marker_color = 'Violet'))

fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["LightlyActiveMinutes"],
    name='Lightly Active',
    marker_color = 'pink'))

fig.update_layout(title_text='Very, Fairy and Lightly Active Minutes Grouped by Days of the Week', title_font_size = 22)

fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()



# In[94]:


# Number of Inactive minutes on each day of the week

day = data["Day"].value_counts()
label = day.index
counts = data["SedentaryMinutes"]
colors = ["DeepSkyBlue", "Tomato", "MediumSeaGreen", "DarkOrange", "MediumPurple", "cyan","SteelBlue"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text = "Inactive Minutes Grouped by Days of the Week",title_font_size = 26)
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size = 20,
                  marker = dict(colors=colors, line=dict(color='black', width=1)))


# In[101]:


#Number of calories burned on each day of the week

calories = data["Day"].value_counts()
label = calories.index
counts = data["Calories"]
colors = ["DeepSkyBlue", "Tomato", "MediumSeaGreen", "DarkOrange", "MediumPurple", "GoldenRod","SteelBlue"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text = "Number of Calories Burned on Each Day of the Week",title_font_size = 26)
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size = 20,
                  marker = dict(colors=colors, line=dict(color='black', width=1)))

