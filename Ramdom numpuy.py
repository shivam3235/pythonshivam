#!/usr/bin/env python
# coding: utf-8

# # Python Random Sampling with Numpy

# In[1]:


import numpy as np
import random


# In[2]:


np.random.random(1)


# In[5]:


np.random.random((3,3))


# In[6]:


np.random.randint(1,4)


# In[7]:


np.random.randint(1,4,(4,4))


# In[8]:


np.random.randint(1,4,(2,4,4))


# In[9]:


np.random.seed(10)
np.random.randint(1,4,(2,4,4))


# In[10]:


np.random.seed(10)
np.random.randint(1,4,(2,4,4))


# In[11]:


2**32 -1


# In[12]:


np.random.rand(3)


# In[13]:


np.random.rand(3,3)


# In[14]:


np.random.randn(3,3)


# In[15]:


x =[1,2,3,4]
np.random.choice(x)


# In[16]:


np.random.choice(x)


# In[17]:


for i in range(20):
    print(np.random.choice(x))


# In[18]:


x


# In[19]:


np.random.permutation(x)


# In[20]:


np.random.permutation(x)


# In[ ]:




