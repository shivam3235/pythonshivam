#!/usr/bin/env python
# coding: utf-8

# # String Operations Comparison and Information

# In[1]:


import numpy as np


# In[2]:


ch_name = " india ai production"
str1 = "Learning python Numpy"


# In[3]:


np.char.add(ch_name,str1)


# In[4]:


np.char.lower(ch_name)


# In[5]:


np.char.upper(str1)


# In[6]:


np.char.upper(ch_name)


# In[8]:


np.char.center(str1,60)


# In[9]:


np.char.center(str1,60,fillchar="*")


# In[10]:


np.char.split(ch_name)


# In[12]:


np.char.splitlines("Hello\nIndia")


# #### 

# In[13]:


str4= "dmy"
str5= "dmy"


# In[14]:


np.char.join([":","/"],[str4,str5])


# In[15]:


np.char.replace(ch_name,"AI","Articial Intelligence")


# In[16]:


np.char.equal(str4,str5)


# In[18]:


np.char.count(ch_name,"a")


# In[19]:


ch_name


# In[20]:


np.char.find(ch_name,'ai')


# In[ ]:




