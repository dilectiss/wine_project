
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


# In[60]:


import numpy as np


# In[61]:


import pandas as pd


# In[62]:


# Import WINE data from .csv files
# Concatenate the smaller tables into one table using pd.concat()
# Create index as name + vintage
# the same shall be done for the RATINGS table
# so that we will have a common index as key
# This is to be done using set_index() function
# Remove duplicates using the drop_duplicates() function


# In[63]:


# Load the raw data files


# In[64]:


wine_rp = pd.read_csv('./data_raw/wine_rp.csv')
wine_bc = pd.read_csv('./data_raw/wine_bc.csv')
wine_bnd = pd.read_csv('./data_raw/wine_bnd.csv')
wine_jr = pd.read_csv('./data_raw/wine_jr.csv')
wine_vag = pd.read_csv('./data_raw/wine_vag.csv')


# In[65]:


frames =  [wine_rp, wine_bc, wine_bnd, wine_jr, wine_vag]


# In[66]:


# Concatenate the five wine_tables using pd.concat on the dataframes


# In[67]:


wines = pd.concat(frames)
wines


# In[68]:


# Create a new 'wine_id' column that is the result of 
# contatenating the 'name' and the 'vintage' columns


# In[69]:


wines['wine_id'] = wines[['name', 'vintage']].apply(lambda x: ''.join(x), axis=1)


# In[70]:


# Set the new index of the WINE table to 'wine_id'


# In[71]:


wines.set_index('wine_id',inplace=True)


# In[72]:


# Convert all currencies to euros and remove signs


# In[73]:


# First remove duplicate parameter labels


# In[74]:


wines = wines[~wines['avg_price'].str.contains("avg_price")]


# In[75]:


# Remove duplicate rows for the final table
# The price is not considered because of errors in currency


# In[76]:


wines_clean = wines.drop_duplicates(subset=['name','vintage','producer','region/appellation','blend','style'])


# In[77]:


# Record the new number of rows


# In[78]:


size_clean = len(wines_clean)
size_clean


# In[79]:


# Remove signs to allow for float conversion
# First remove the dollar signs, space, commas


# In[80]:


wines_clean = wines_clean.replace({'\n':''}, regex = True)
wines_clean['avg_price'] = wines_clean['avg_price'].replace({'\$':''},regex = True)
wines_clean['avg_price'] = wines_clean['avg_price'].replace({'\,':''},regex = True)
wines_clean['avg_price'] = wines_clean['avg_price'].replace({'\ ':''},regex = True)


# In[81]:


# Converting Kč into EUR


# In[82]:


for i in range(0, size_clean):
    if 'Kč' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('Kč', '')
        j = float(j) * 0.039
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[83]:


# Converting Rb into EUR


# In[84]:


for i in range(0, size_clean):
    if 'Rb' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('Rb', '')
        j = float(j) * 0.013
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[85]:


# Converting Kr into EUR


# In[86]:


for i in range(0, size_clean):
    if 'Kr' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('Kr', '')
        j = float(j) * 0.095
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[87]:


for i in range(0, size_clean):
    if 'kr' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('kr', '')
        j = float(j) * 0.095
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[88]:


# Converting S$ into EUR


# In[89]:


for i in range(0, size_clean):
    if 'S' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('S', '')
        j = float(j) * 0.065
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[90]:


# Converting HK into EUR


# In[91]:


for i in range(0, size_clean):
    if 'HK' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('HK', '')
        j = float(j) * 0.11
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[92]:


# Converting CA into EUR


# In[93]:


for i in range(0, size_clean):
    if 'CA' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('CA', '')
        j = float(j) * 0.67
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[94]:


# Converting £ into EUR


# In[95]:


for i in range(0, size_clean):
    if '£' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('£', '')
        j = float(j) * 1.17
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[96]:


# Converting CHF into EUR


# In[97]:


for i in range(0, size_clean):
    if 'CHF' in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = j.replace('CHF', '')
        j = float(j) * 0.88
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[98]:


# Converting $ into EUR


# In[99]:


for i in range(0, size_clean):
     if '€' not in wines_clean['avg_price'].iloc[i]:
        j = wines_clean['avg_price'].iloc[i]
        j = float(j) * 0.88
        j = str(j)
        wines_clean['avg_price'].iloc[i] = j


# In[100]:


# Finally, remove all signs and convert strings to float


# In[101]:


wines_clean['avg_price'] = wines_clean['avg_price'].replace({'\€':''},regex = True)
wines_clean['avg_price'] = pd.to_numeric(wines_clean['avg_price'])


# In[102]:


#The cleaned wines table


# In[103]:


wines_clean


# In[104]:


# Record the number of rows of the original wines


# In[105]:


size_raw = len(wines)
size_raw


# In[106]:


# Compute the number of duplicates


# In[107]:


duplicates=size_raw - size_clean
duplicates


# In[108]:


"""Duplicates = 11709 as of data from 28.02.2019"""


# In[109]:


# Export to csv


# In[110]:


wines_clean.to_csv(r'./wines_clean.csv')

