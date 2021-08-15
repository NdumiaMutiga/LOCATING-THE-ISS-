#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing the Packages 
import pandas as pd
import plotly.express as px


# In[3]:


url='http://api.open-notify.org/iss-now.json'


# In[4]:


df=pd.read_json(url)


# In[5]:


df


# In[6]:


df['latitude']=df.loc['latitude','iss_position']
df['longitude']=df.loc['longitude','iss_position']
df.reset_index(inplace=True)


# In[7]:


df


# In[8]:


df=df.drop(['index', 'message'], axis=1)


# In[9]:


df


# In[11]:


fig=px.scatter_geo(df, lat='latitude', lon='longitude')
fig.show()


# In[ ]:




