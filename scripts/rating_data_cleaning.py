
# coding: utf-8
# {
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
# In[58]:


import numpy as np
import pandas as pd
import pyreadr as pr


# In[59]:


# Import RATINGS data from .rds files
# Create index as name + vintage
# as has been done in the WINE table
# so that we will have a common index as key
# This is to be done using set_index() function


# In[60]:


# Load the .rds file
# Data from https://arc-git.mpib-berlin.mpg.de/taste/wine/wine-searcher/tree/master/output


# In[61]:


ratings = pr.read_r('./data_raw/critics_ratings.rds')


# In[62]:


# Load the .csv file for critics


# In[63]:


critics = pd.read_csv('./data_raw/critic_id.csv')


# In[64]:


# Extract the pandas dataframe


# In[65]:


ratings = ratings[None]


# In[66]:


# Rename the columns


# In[67]:


ratings.columns = ['name', 'vintage','popularity','score','avg_price','critic']


# In[68]:


# Convert types to strings to prepare for concatenation


# In[69]:


ratings['vintage'] = ratings['vintage'].astype(str)
ratings['name'] = ratings['name'].astype(str)


# In[70]:


# Create a new 'wine_id' column that is the result of 
# contatenating the 'name' and the 'vintage' columns


# In[71]:


ratings['wine_id'] = ratings[['name', 'vintage']].apply(lambda x: ''.join(x), axis=1)


# In[72]:


# Drop redundant columns


# In[73]:


ratings = ratings.drop(columns=['name', 'vintage','avg_price'])


# In[74]:


# Set the index of the new RATINGS table to 'critic'


# In[75]:


ratings.set_index('critic',inplace=True)


# In[79]:


# Set the index of the CRITICS table to 'critic_name'


# In[80]:


critics.set_index('critic_name',inplace=True)


# In[ ]:


# Merge the tables upon index


# In[87]:


ratings = ratings.merge(critics, left_index=True, right_index=True)


# In[ ]:


# Set the index of RATINGS to 'wine_id'


# In[89]:


ratings.set_index('wine_id',inplace=True)


# In[ ]:


# Sort the order of the columns


# In[94]:


ratings = ratings[['critic_id','score','popularity']]


# In[95]:


ratings


# In[96]:


# Export to .csv


# In[97]:


ratings.to_csv(r'./ratings_clean.csv')

