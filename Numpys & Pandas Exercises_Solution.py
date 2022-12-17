#!/usr/bin/env python
# coding: utf-8

# # Learning Numpy

# In[1]:


import numpy as np 


# ### Creating Arrays

# <strong><ins>All arrays mentioned here are numpy arrays as long as opposite is not mentioned</ins></strong> please solve the problems with this knowledge.

# Create an array in size of 4*3 and assing it to arr variable 

# In[5]:


arr = np.eye(4,3)
print(arr)


# Create an array with elements from 0 to 15 (both inclusive) and assing it to arr2 variable   
# Then print the shape of the arr2  
# copy the arr2 to arr2_copy  
# print arr2, arr2_copy   
# Change its shape to 4*4 and assign to itself   
# print arr2, arr2_copy again    

# In[4]:


arr2 = np.arange(16)
arr2_copy = arr2.copy()


# In[5]:


print(arr2)


# In[6]:


print(arr2_copy)


# In[7]:


arr2 = arr2.reshape(4,4)


# In[8]:


print(arr2)


# In[9]:


print(arr2_copy)


# ### Some Functions 

# ##### How many dimentions there are in arr2 variable? 

# In[10]:


arr2.ndim


# ##### Describe the number of rows and columns in arr2 variable 

# In[11]:


arr2.shape


# ##### How many elements there are in arr2 variable?

# In[12]:


arr2.size


# ##### Print the data type of arr2

# In[13]:


arr2.dtype


# #### Print the data location in the memory

# In[14]:


arr2.data


# ### Some Statistics About the Arrays

# #### Show 50th percentile of arr2

# In[15]:


np.percentile(arr2, 50)


# #### Show mean of arr2 elements

# In[16]:


np.mean(arr2)


# #### Show median of arr2 elements

# In[17]:


np.median(arr2)


# ##### Create one dimensional normally distrubuted array with mean 3 standard deviation is 4 and has elements of 100

# In[23]:





# In[12]:


s = np.random.normal(loc=3, scale=4, size=100)
s


# #### Install matplotlib library for ploting purposes and then plot the s 
# - search to find how to do

# In[14]:


import matplotlib.pyplot as plt


s = np.random.normal(loc=3, scale=4, size=100)
fig, ax = plt.subplots()
plt.hist(s, width=4, edgecolor="blue", linewidth=0, density=False)
plt.show()


# ____

# # Learning Pandas

# ##### Read the airline safety data assign to df variable and print first 5 rows with pandas function

# In[6]:


import pandas as pd 


# In[7]:


df = pd.read_csv(r'E:\Επιφάνεια Εργασίας Μου\Develhope\EXERCISES\Numpy_Pandas\airline_safety_data.txt')


# In[18]:


df.head()


# ##### print last 5 rows with pandas function

# In[19]:


df.tail()


# ##### Show shape of df

# In[20]:


df.shape


# ##### Show descriptive statistics of df

# In[21]:


df.describe()


# #### Show df column informations

# In[22]:


df.info()


# #### Select companies and incidents_85_99 with incidents_85_99 is less than 10

# In[23]:


df.loc[df.incidents_85_99 < 10, ['airline','incidents_85_99']]


# #### Group companies by first letter(lower) and take the mean incidents_85_99 and make it a dataframe again 

# In[11]:


def lowerit(value): 
    value=value.lower() 
    return value 
df['firstletter'] = df['airline'].str[0].apply(lowerit) 
firstletter=df.groupby('firstletter')['incidents_85_99'].mean()
firstletter=firstletter.to_frame()
firstletter


# In[67]:




