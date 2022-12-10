#!/usr/bin/env python
# coding: utf-8

# # Learning Numpy

# In[3]:


import numpy as np 


# ### Creating Arrays

# <strong><ins>All arrays mentioned here are numpy arrays as long as opposite is not mentioned</ins></strong> please solve the problems with this knowledge.

# Create an array in size of 4*3 and assing it to arr variable 

# In[2]:


arr = np.array([4,3])


# Create an array with elements from 0 to 15 (both inclusive) and assing it to arr2 variable   
# Then print the shape of the arr2  
# copy the arr2 to arr2_copy  
# print arr2, arr2_copy   
# Change its shape to 4*4 and assign to itself   
# print arr2, arr2_copy again    

# In[19]:


arr2 = np.arange(16)
arr2_copy = arr2.copy()


# In[12]:


print(arr2)


# In[13]:


print(arr2_copy)


# In[20]:


arr2 = arr2.reshape(4,4)


# In[21]:


print(arr2)


# In[18]:


print(arr2_copy)


# ### Some Functions 

# ##### How many dimentions there are in arr2 variable? 

# In[22]:


arr2.ndim


# ##### Describe the number of rows and columns in arr2 variable 

# In[23]:


arr2.shape


# ##### How many elements there are in arr2 variable?

# In[24]:


arr2.size


# ##### Print the data type of arr2

# In[25]:


arr2.dtype


# #### Print the data location in the memory

# In[26]:


arr2.data


# ### Some Statistics About the Arrays

# #### Show 50th percentile of arr2

# In[26]:


np._(_, _)


# #### Show mean of arr2 elements

# In[30]:


np._(_)


# #### Show median of arr2 elements

# In[33]:


np._(_)


# ##### Create one dimensional normally distrubuted array with mean 3 standard deviation is 4 and has elements of 100

# In[34]:


from numpy import _


# In[36]:


s = np._._(_, _, _)


# #### Install matplotlib library for ploting purposes and then plot the s 
# - search to find how to do

# In[42]:


import matplotlib.pyplot as plt
_
_
_


# ____

# # Learning Pandas

# ##### Read the airline safety data assign to df variable and print first 5 rows with pandas function

# In[43]:


import _ as pd 


# In[44]:


df = _


# In[45]:


df._


# ##### print last 5 rows with pandas function

# In[46]:


df._


# ##### Show shape of df

# In[47]:


df._


# ##### Show descriptive statistics of df

# In[51]:


df._


# #### Show df column informations

# In[56]:


df._


# #### Select companies and incidents_85_99 with incidents_85_99 is less than 10

# In[60]:


_


# #### Group companies by first letter(lower) and take the mean incidents_85_99 and make it a dataframe again 

# In[65]:


_


# In[67]:


_

