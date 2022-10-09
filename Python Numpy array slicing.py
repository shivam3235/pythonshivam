#!/usr/bin/env python
# coding: utf-8

# # Python Numpy array slicing:

# In[1]:


import numpy as np


# 

# In[3]:


mx =np.arange(1,101).reshape(10,10)
print(mx)


# In[4]:


mx[0,0]


# In[5]:


mx[0,0].ndim


# In[6]:


mx[0]


# In[7]:


mx[:,0]


# In[8]:


mx[:,0:1]


# In[9]:


mx[:,0:1].ndim


# In[10]:


mx


# In[11]:


mx[1:4,1:4]


# In[12]:


mx[:,1:3]


# In[13]:


mx[:]


# In[14]:


mx[::]


# In[15]:


mx[:,:]


# In[16]:


mx.itemsize


# In[17]:


mx.dtype


# In[18]:


32/8


# In[ ]:




