#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_excel('colors.xlsx');


# In[15]:





# In[4]:


df2 = df.sort_values('HEX',ascending=False)


# In[5]:


df2.to_excel('sorted_colors.xlsx')


# In[6]:


df2


# In[ ]:




