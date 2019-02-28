
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


import pandas as pd


# In[11]:


# Import WINE data from .csv files
#
# Concatenate the smaller tables into one table using pd.concat()
#
# Create index as name + vintage
# the same shall be done for the RATINGS table
# so that we will have a common index as key
# This is to be done using set_index() function
#
# Remove duplicates using the drop_duplicates() function


# In[ ]:


# Load the raw data files


# In[63]:


wine_rp = pd.read_csv('./data_raw/wine_rp.csv')
wine_bc = pd.read_csv('./data_raw/wine_bc.csv')
wine_bnd = pd.read_csv('./data_raw/wine_bnd.csv')
wine_jr = pd.read_csv('./data_raw/wine_jr.csv')
wine_vag = pd.read_csv('./data_raw/wine_vag.csv')


# In[64]:


frames =  [wine_rp, wine_bc, wine_bnd, wine_jr, wine_vag]


# In[65]:


# Concatenate the five wine_tables using pd.concat on the dataframes


# In[66]:


wines = pd.concat(frames)


# In[67]:


# Create a new 'index' column that is the result of 
# contatenating the 'name' and the 'vintage' columns


# In[68]:


wines['index'] = wines[['name', 'vintage']].apply(lambda x: ''.join(x), axis=1)


# In[69]:


# Set the new index of the WINE table to 'index'


# In[70]:


wines.set_index('index',inplace=True)


# In[71]:


# Record the number of rows of the original wines


# In[83]:


size_raw = len(wines)


# In[73]:


# Remove duplicate rows


# In[90]:


wines_clean = wines.drop_duplicates()
wines_clean


# In[75]:


# Record the new number of rows


# In[89]:


size_clean = len(wines_clean)
size_clean


# In[ ]:


# Compute the number of duplicates


# In[87]:


duplicates=size_raw - size_clean
duplicates


# In[ ]:


"""Duplicates = 3398 as of data from 28.02.2019"""


# In[ ]:


# Export to csv


# In[88]:


wines_clean.to_csv(r'./wines_clean.csv')

