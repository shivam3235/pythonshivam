#!/usr/bin/env python
# coding: utf-8

# #dictionariesa python

# In[3]:


d1= {}
print(d1)
print(type(d1))


# In[5]:


d2={1:"welocme", 2: "to", 3: "python", 4:"tutorial"}
print(d2)


# 

# In[7]:


d3={"name":"sam","age":22,"profession": "student"}
print(d3)


# In[8]:


d4 =dict({1:"welocme", 2: "to", 3: "python", 4:"tutorial"})
print(d4)


# In[11]:


d5=dict([(1,"welcome"),(2,"to"),(3,"python"),(4,"tutorial")])
print(d5)


# In[14]:


d6={"name":{"first":"sam", "last":"crew"},"age":22,"profession": "student"}
print(d6)


# #Adding Element

# In[18]:


d={}
d[0]="welcome"
print(d)


# In[21]:


d[1]="How","are" ,"you"
print(d)


# In[23]:


d["name"]="sam"
print(d)


# In[24]:


d["name"]={"first": "sam","last":"crew"}
print(d)


# #Accessing Element

# In[26]:


print(d)


# In[29]:


print(d["name"])


# In[30]:


printprint(d["name"])


# In[31]:


print(d["name"]["first"])


# In[32]:


print(d.get(1))


# Deleting  Element

# In[34]:


print(d)


# In[35]:


d.pop(0)


# In[36]:


print(d)


# In[37]:


d.popitem()


# In[38]:


print(d)


# In[39]:


print(d)


# Uing bulit in function

# In[41]:


d.values()


# In[43]:


keys={'a','b','c','d'}
value=1
dict.fromkeys(keys,value)


# In[44]:


d.clear()


# In[45]:


print(d)


# Set

# In[47]:


s = set({1,2,3,4})
print(s)
print(type(s))


# In[48]:


s.add('a')
print(s)


# In[49]:


fs=frozenset([1,2,3,4])
print(fs)


# In[50]:


fd.add('a')


# In[51]:


s1=set([1,2,3,4])
s2=set({2,3,4,5})
s1.union(s2)


# In[52]:


s1.difference(s2)


# In[ ]:




