#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# In[3]:


data = pd.read_csv('C:/Users/PP/Desktop/Netzwerk assignments/ML Assignments/Visitor_Prediction_Multiple_Linear_Regression_data.csv')


# In[5]:


data.head()


# In[7]:


data.shape


# In[8]:


data = data.drop('Unnamed: 7',axis = 1)


# In[10]:


data.head(20)


# In[11]:


x = data.drop(data.columns[[0,2]],axis=1)


# In[15]:


x.head()


# In[19]:


y = data.Visitors


# In[21]:


y.head()


# In[22]:


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=12)


# In[23]:


reg = LinearRegression()


# In[24]:


reg.fit(x_train, y_train)


# In[25]:


pred = reg.predict(x_test)


# In[26]:


pred


# In[27]:


y_test


# In[28]:


r2_score(y_test,pred)


# In[40]:


plt.plot(x,y)
plt.xlabel("Show,Platform, Ad_impression, Cricket, Character_A")
plt.ylabel("Visitors")
plt.show()


# In[ ]:




