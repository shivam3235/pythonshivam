#!/usr/bin/env python
# coding: utf-8

# # Find Trignometry sin() cos() and tan() using Numpy Trignometry Functions

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[4]:


np.sin(180)


# In[5]:


np.sin(90)


# In[6]:


np.cos(180)


# In[7]:


np.cos(90)


# In[8]:


np.tan(180)


# In[9]:


np.tan(90)


# In[13]:


x_sin = np.arange(0,3*np.pi,0.1)
print(x_sin)


# In[ ]:





# In[14]:


y_sin = np.sin(x_sin)
print(y_sin)


# In[15]:


plt.plot(x_sin,y_sin)
plt.show()


# In[17]:


y_cos = np.cos(x_sin)
plt.plot(x_sin,y_cos)
plt.show()


# In[19]:


y_tan = np.tan(x_sin)
plt.plot(x_sin,y_tan)
plt.show()


# In[ ]:




