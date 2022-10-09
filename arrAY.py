#!/usr/bin/env python
# coding: utf-8

# # Array

# In[2]:


from array import *
arr = array('i',[-1,2,3,4,5,])
print(arr)


# In[3]:


print(arr.buffer_info())


# In[4]:


print(arr(2))


# In[5]:


print([2])


# In[6]:


print(arr[2])


# In[7]:


for i in arr:
    print(i)


# In[8]:


for pnt in range(5):
    print(arr[pnt])


# In[12]:


for pnt in range(5):
    print(pnt,arr[pnt])


# In[14]:


for put in range(1,4):
    print(pnt,arr[pnt])


# In[15]:


arr.reverse()
print(arr)


# In[16]:


arr.append(10)
print(arr)


# In[19]:


arr = array('i',[-1,2,2,3,4,5])
arr.remove(2)
print(arr)


# In[21]:


arr = array('i',[-1,2,3,4,5])
print(arr[3])
print(arr.index(2))


# In[23]:


arr = array('i',[])
print(arr)


# In[ ]:


arr = array("i",[])
x = int(input("Enter the sixe of array"))
print('Enter %d the elements'%x)


# In[ ]:


from array import *
arr = array("i",[])
x = int(input("Enter the sixe of array"))
print('Enter the %d element'%x)


# # functon

# In[ ]:


def hello():
    printf("Shivam")
hello()    
    
    


# In[ ]:




