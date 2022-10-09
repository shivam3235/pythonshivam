#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr_1d=np.array([1,2,3,4])


# In[3]:


print(arr_1d)


# In[4]:


type(arr_1d)


# In[5]:


arr_1d.ndim


# In[6]:


arr_2d=np.array([[1,2,3,4],[5,6,7,8]])


# In[7]:


print(arr_2d)


# In[10]:


arr_2d.ndim


# In[11]:


arr_1d.size


# In[12]:


arr_2d.size


# In[13]:


arr_2d.shape


# In[14]:


arr_1d.shape


# In[15]:


arr_2d.dtype


# In[16]:


arr_1d.dtype


# In[18]:


mx_1s =np.array([[1,1,1],[1,1,1],[1,1,1]])


# In[19]:


print(mx_1s)


# In[20]:


np.ones(5)


# In[21]:


mx_1s= np.ones(5)


# In[22]:


print(mx_1s)


# In[23]:


mx_1s.dtype


# In[24]:


mx_1s=np.ones((3,4))


# In[25]:


print(mx_1s)


# In[31]:


mx_1s=np.ones((3,4),dtype= int)


# In[30]:


mx_1s=np.ones((3,4),dtype = int)
print(mx_1s)


# In[32]:


mx_1s=np.zeros((4,6))


# In[33]:


print(mx_1s)


# In[36]:


ms_1s= np.zeros((4,6),dtype =bool)


# In[37]:


print(ms_1s)


# In[38]:


ms_1s= np.zeros((4,6),dtype =str)


# In[39]:


print(ms_1s)


# In[40]:


em_str = ''


# In[41]:


print(bool(em_str))


# In[42]:


em_mx =np.empty((3,3))


# In[43]:


print(em_mx)


# # Mathematic Operation using Numpy

# In[44]:


arr1 =np.arange(1,10).reshape(3,3)
arr2 =np.arange(1,10).reshape(3,3)
print(arr1)
print(arr2)


# In[45]:


arr1+arr2


# In[47]:


np.add(arr1,arr2)


# In[48]:


arr1-arr2


# In[49]:


np.subtract(arr1,arr2)


# In[50]:


arr1/ arr2


# In[51]:


np.divide(arr1,arr2)


# In[52]:


arr1 * arr2


# In[53]:


print(arr1)
print(arr2)


# In[54]:


np.multiply(arr1,arr2)


# In[55]:


arr1 @arr2


# In[56]:


arr1.dot(arr2)


# In[57]:


arr1


# In[59]:


arr1.max()


# In[60]:


arr1.argmax()


# In[61]:


arr1.max(axis=0)


# In[62]:


arr1.max(axis=1)


# In[63]:


arr1.min()


# In[64]:


arr1.argmin()


# In[65]:


arr1.min(axis=0)


# In[66]:


arr1


# In[67]:


np.sum(arr1)


# In[68]:


np.sum(arr1,axis=0)


# In[69]:


np.sum(arr1,axis=1)


# In[70]:


np.mean(arr1)


# In[71]:


np.sqrt(arr1)


# In[73]:


np.std(arr1)


# In[74]:


np.exp(arr1)


# In[75]:


np.log(arr1)


# In[76]:


np.log10(arr1)


# # Numpy Functions:

# In[ ]:


# Arange()


# In[79]:


np_1d= np.arange(1,13)


# In[80]:


print(np_1d)


# In[81]:


even_arr=np.arange(1,13,2)


# In[83]:


print(even_arr)


# In[ ]:


# linspace


# In[84]:


np.linspace(1,5,4)


# In[ ]:


#reshape


# In[92]:


ar_2d=ar_1d.reshape(2,6)
print(ar_2d)


# In[ ]:


#ravel


# In[93]:


ar.ravel()


# In[ ]:




