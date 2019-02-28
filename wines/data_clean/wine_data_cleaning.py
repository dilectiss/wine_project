
# coding: utf-8

# In[452]:


import numpy as np


# In[453]:


import pandas as pd


# In[454]:


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


# In[455]:


# Load the raw data files

wine_rp = pd.read_csv('./data_raw/wine_rp.csv')
wine_bc = pd.read_csv('./data_raw/wine_bc.csv')
wine_bnd = pd.read_csv('./data_raw/wine_bnd.csv')
wine_jr = pd.read_csv('./data_raw/wine_jr.csv')
wine_vag = pd.read_csv('./data_raw/wine_vag.csv')


# In[456]:


frames =  [wine_rp, wine_bc, wine_bnd, wine_jr, wine_vag]


# In[457]:


# Concatenate the five wine_tables using pd.concat on the dataframes
wines = pd.concat(frames)
wines


# In[458]:


# Create a new 'index' column that is the result of 
# contatenating the 'name' and the 'vintage' columns

wines['index'] = wines[['name', 'vintage']].apply(lambda x: ''.join(x), axis=1)


# In[459]:


# Set the new index of the WINE table to 'index'

wines.set_index('index',inplace=True)


# In[460]:


# Convert all currencies to euros and remove signs


# In[461]:


# First remove duplicate parameter labels

wines = wines[~wines['avg_price'].str.contains("avg_price")]


# In[462]:


# Remove duplicate rows for the final table
# The price is not considered because of errors in currency

wines_clean = wines.drop_duplicates(subset=['name','vintage','producer','region/appellation','blend','style'])


# In[463]:


# Record the new number of rows

size_clean = len(wines_clean)
size_clean


# In[464]:


# Remove signs to allow for float conversion
# First remove the dollar signs, space, commas

wines_clean = wines_clean.replace({'\n':''}, regex = True)
wines_clean['avg_price'] = wines_clean['avg_price'].replace({'\$':''},regex = True)
wines_clean['avg_price'] = wines_clean['avg_price'].replace({'\,':''},regex = True)
wines_clean['avg_price'] = wines_clean['avg_price'].replace({'\ ':''},regex = True)


# In[465]:


# Converting Kč into EUR 
for i in range(0, size_clean):
    if 'Kč' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('Kč', '')
        j = float(j) * 0.039
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[466]:


# Converting Rb into EUR 
for i in range(0, size_clean):
    if 'Rb' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('Rb', '')
        j = float(j) * 0.013
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[467]:


# Converting Kr into EUR 
for i in range(0, size_clean):
    if 'Kr' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('Kr', '')
        j = float(j) * 0.095
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[468]:


for i in range(0, size_clean):
    if 'kr' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('kr', '')
        j = float(j) * 0.095
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[469]:


# Converting S$ into EUR 
for i in range(0, size_clean):
    if 'S' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('S', '')
        j = float(j) * 0.065
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[470]:


# Converting HK into EUR
for i in range(0, size_clean):
    if 'HK' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('HK', '')
        j = float(j) * 0.11
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[471]:


# Converting CA into EUR
for i in range(0, size_clean):
    if 'CA' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('CA', '')
        j = float(j) * 0.67
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[472]:


# Converting £ into EUR 
for i in range(0, size_clean):
    if '£' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('£', '')
        j = float(j) * 1.17
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[473]:


# Converting CHF into EUR 
for i in range(0, size_clean):
    if 'CHF' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('CHF', '')
        j = float(j) * 0.88
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[474]:


# Converting $ into EUR
for i in range(0, size_clean):
     if '€' not in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = float(j) * 0.88
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[475]:


# Finally, remove all signs and convert strings to float
wines_clean['avg_price'] = wines_clean['avg_price'].replace({'\€':''},regex = True)
wines_clean['avg_price'] = pd.to_numeric(wines_clean['avg_price'])


# In[476]:


#The cleaned wines table

wines_clean


# In[477]:


# Record the number of rows of the original wines

size_raw = len(wines)
size_raw


# In[478]:


# Compute the number of duplicates

duplicates=size_raw - size_clean
duplicates


# In[447]:


"""Duplicates = 11709 as of data from 28.02.2019"""


# In[448]:


# Export to csv

wines_clean.to_csv(r'./wines_clean.csv')

