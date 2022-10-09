#!/usr/bin/env python
# coding: utf-8

# # How to create python panadas DataFrame

# In[1]:


import pandas as pd


# In[2]:


emt_df =pd.DataFrame()
print(emt_df)


# In[3]:


lst =['a','b','c']
print(lst)


# In[4]:


df1 = pd.DataFrame(lst)
print(df1)


# In[5]:


df1


# In[8]:


ls_of_ls =[[1,2,3,],[2,3,4],[4,5,6]]
print(ls_of_ls)


# 

# In[9]:


df2 = pd.DataFrame(ls_of_ls)
df2


# In[10]:


dict1 ={'ID':[11,22,33,44]}
dict1


# In[12]:


dict3 = pd.DataFrame(dict1)
dict3


# In[13]:


dict1 ={'ID':[11,22,33,44],'SN':[1,2,3,4]}
dict1


# In[14]:


df3 =pd.DataFrame(dict1)


# In[15]:


df3


# In[16]:


ls_dict = [{'a':1,'b':2},{'a':3,'b':4}]
df5 =pd.DataFrame(ls_dict)
df5


# In[17]:


ls_dict = [{'a':1,'b':2},{'a':3,'b':4,'c':5}]
df5 =pd.DataFrame(ls_dict)
df5


# In[19]:


dict_sr ={'Id':pd.Series([1,2,3]),'SN':pd.Series([111,222,333])}
df6 = pd.DataFrame(dict_sr)
df6


# In[ ]:




