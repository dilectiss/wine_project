
# coding: utf-8

# In[ ]:


{
  "celltoolbar": "Raw Cell Format",
  "kernelspec": {
    "name": "python3",
    "display_name": "Python 3",
    "language": "python"
  },
  "language_info": {
    "name": "python",
    "version": "3.6.8",
    "mimetype": "text/x-python",
    "codemirror_mode": {
      "name": "ipython",
      "version": 3
    },
    "pygments_lexer": "ipython3",
    "nbconvert_exporter": "python",
    "file_extension": ".py"
  }
}


# In[452]:


import numpy as np


# In[453]:


import pandas as pd


# In[ ]:


# Import WINE data from .csv files
# Concatenate the smaller tables into one table using pd.concat()
# Create index as name + vintage
# the same shall be done for the RATINGS table
# so that we will have a common index as key
# This is to be done using set_index() function
# Remove duplicates using the drop_duplicates() function


# In[ ]:


# Load the raw data files


# In[455]:


wine_rp = pd.read_csv('./data_raw/wine_rp.csv')
wine_bc = pd.read_csv('./data_raw/wine_bc.csv')
wine_bnd = pd.read_csv('./data_raw/wine_bnd.csv')
wine_jr = pd.read_csv('./data_raw/wine_jr.csv')
wine_vag = pd.read_csv('./data_raw/wine_vag.csv')


# In[456]:


frames =  [wine_rp, wine_bc, wine_bnd, wine_jr, wine_vag]


# In[ ]:


# Concatenate the five wine_tables using pd.concat on the dataframes


# In[457]:


wines = pd.concat(frames)
wines


# In[ ]:


# Create a new 'index' column that is the result of 
# contatenating the 'name' and the 'vintage' columns


# In[458]:


wines['index'] = wines[['name', 'vintage']].apply(lambda x: ''.join(x), axis=1)


# In[ ]:


# Set the new index of the WINE table to 'index'


# In[459]:


wines.set_index('index',inplace=True)


# In[460]:


# Convert all currencies to euros and remove signs


# In[ ]:


# First remove duplicate parameter labels


# In[461]:


wines = wines[~wines['avg_price'].str.contains("avg_price")]


# In[ ]:


# Remove duplicate rows for the final table
# The price is not considered because of errors in currency


# In[462]:


wines_clean = wines.drop_duplicates(subset=['name','vintage','producer','region/appellation','blend','style'])


# In[ ]:


# Record the new number of rows


# In[463]:


size_clean = len(wines_clean)
size_clean


# In[ ]:


# Remove signs to allow for float conversion
# First remove the dollar signs, space, commas


# In[464]:


wines_clean = wines_clean.replace({'\n':''}, regex = True)
wines_clean['avg_price'] = wines_clean['avg_price'].replace({'\$':''},regex = True)
wines_clean['avg_price'] = wines_clean['avg_price'].replace({'\,':''},regex = True)
wines_clean['avg_price'] = wines_clean['avg_price'].replace({'\ ':''},regex = True)


# In[ ]:


# Converting Kč into EUR


# In[465]:


for i in range(0, size_clean):
    if 'Kč' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('Kč', '')
        j = float(j) * 0.039
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[ ]:


# Converting Rb into EUR


# In[466]:


for i in range(0, size_clean):
    if 'Rb' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('Rb', '')
        j = float(j) * 0.013
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[ ]:


# Converting Kr into EUR


# In[467]:


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


# In[ ]:


# Converting S$ into EUR


# In[469]:


for i in range(0, size_clean):
    if 'S' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('S', '')
        j = float(j) * 0.065
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[ ]:


# Converting HK into EUR


# In[470]:


for i in range(0, size_clean):
    if 'HK' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('HK', '')
        j = float(j) * 0.11
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[ ]:


# Converting CA into EUR


# In[471]:


for i in range(0, size_clean):
    if 'CA' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('CA', '')
        j = float(j) * 0.67
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[ ]:


# Converting £ into EUR


# In[472]:


for i in range(0, size_clean):
    if '£' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('£', '')
        j = float(j) * 1.17
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[ ]:


# Converting CHF into EUR


# In[473]:


for i in range(0, size_clean):
    if 'CHF' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('CHF', '')
        j = float(j) * 0.88
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[ ]:


# Converting $ into EUR


# In[474]:


for i in range(0, size_clean):
     if '€' not in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = float(j) * 0.88
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[ ]:


# Finally, remove all signs and convert strings to float


# In[475]:


wines_clean['avg_price'] = wines_clean['avg_price'].replace({'\€':''},regex = True)
wines_clean['avg_price'] = pd.to_numeric(wines_clean['avg_price'])


# In[ ]:


#The cleaned wines table


# In[476]:


wines_clean


# In[ ]:


# Record the number of rows of the original wines


# In[477]:


size_raw = len(wines)
size_raw


# In[ ]:


# Compute the number of duplicates


# In[478]:


duplicates=size_raw - size_clean
duplicates


# In[447]:


"""Duplicates = 11709 as of data from 28.02.2019"""


# In[ ]:


# Export to csv


# In[448]:


wines_clean.to_csv(r'./wines_clean.csv')

