#!/usr/bin/env python
# coding: utf-8

# # Assignment _ 28-02-2023 (Plotly Visualization)

# ## Q1. Load the "titanic" dataset using the load_dataset function of seaborn. use plotly express to plot a scatter plot for age and fare columns in the titanic data set.
# 
# ### Ans:-
# 

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# In[2]:


titanic = sns.load_dataset("titanic")
titanic.tail()


# In[3]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=titanic.age,y=titanic.fare,mode='markers'))


# In[4]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=titanic.age,y=titanic.fare,mode='lines'))


# ## Q2. Using the tips dataset in the plotly library, plot a boxplot using plotly express.
# 
# ### Ans:-

# In[5]:


import plotly.express as px

# Load the tips dataset
tips = px.data.tips()

# Create a boxplot using plotly express

fig = px.box(tips,x='day',y='total_bill')

fig.show()


# In[6]:


# Load the tips dataset
tips = px.data.tips()

# Create a boxplot using plotly express

fig = px.box(tips,x='day',y='tip')

fig.show()


# ## Q3. Using the tips dataset in the plotly library, plot a histogram for x='sex' and y='total_bill' column in the tips dataset. Also use the "Smoker" column with the patteren_shape parameter and the 'day' column with the color parameter.
# 
# ### Ans:-

# In[7]:


tips = px.data.tips()
fig = px.histogram(tips,x='sex',y='total_bill',color='day',pattern_shape='smoker',barmode='group')
fig.show()


# ## Q5. What is Distplot? using plotly express, plot a distplot?
# 
# ### Ans:-
# 
#         Distplot is a function in the plotly express library that creates a combination of a histogram and a kernel density
#         estimate (KDE) plot. It visualizes the distribution of a continuous variable by showing the density estimate and the 
#         underlying histogram of the data.

# In[8]:


tips = px.data.tips()
fig = px.histogram(tips,x = 'total_bill',nbins= 20 , opacity=0.5,marginal= 'box')
fig.show()


# ## Q4. Using the iris dataset in the plotly library , plot a scatter matrix plot,using the "species" column for the color parameter.
# 
# ### Note :- Use "sepal_length',sepal_width','Petal_length',Petal_width columns only with the dimensions parameter.
# 
# ## Ans:-

# In[9]:


iris = px.data.iris()
iris


# In[10]:


fig = px.scatter_matrix(iris,dimensions=['sepal_length','sepal_width','petal_length','petal_width'],color='species')
fig.show()


# In[ ]:




