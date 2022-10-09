#!/usr/bin/env python
# coding: utf-8

# 

# In[1]:


num=5
type(num)


# In[2]:


num=1214235
type(num)


# In[3]:


num=3.2
type(num)


# In[4]:


num=2+5j
type(num)


# In[5]:


num.real


# In[6]:


num.imag


# In[7]:


num=-23453.899
num


# In[8]:


num1=10
num2=20
print(num1+num2)


# In[9]:


print(num1-num2)


# In[10]:


print(num1%num2)


# In[11]:


print(num1*num2)


# In[12]:


print(num1/num2)


# In[14]:


print(10/3)


# In[15]:


print(10//3)


# In[16]:


print(num1**num2)


# In[17]:


print(num1*num2)


# In[18]:


print(num1%num2)


# In[19]:


print(10/3)


# In[20]:


x ="192"
type(x)


# In[21]:


int(x)


# In[23]:


x = int(x)
type(x)


# In[24]:


x= float(x)


# In[25]:


print(x)


# In[26]:


x= complex(x)


# In[27]:


print(x)


# In[28]:


print(complex(2,0))


# # Functions

# In[29]:


x = -7.5
print(abs(x))


# In[31]:


import math
x= 10
print(math.exp(x))


# In[32]:


math.e


# In[33]:


math.pi


# In[34]:


print(math.sqrt(6))


# In[35]:


max(1,233,43,5,65)


# In[36]:


min(2344,456,5766,3243)


# # Creating lists
#   

# In[37]:


num=[1,2,3,4]


# In[38]:


print(num)


# In[39]:


letter=['a','b','c','c']


# In[40]:


print(letter)


# In[41]:


stg=["get","shivam","ankit"]


# In[44]:


print(stg)


# In[46]:


print(stg)


# In[47]:


mix=[1,6,"shivam","get","certfied"]


# In[48]:


print(mix)


# In[51]:


mat=[[1,2],[['a','b']]
print(mat)


#  # Accessing Element list

# In[52]:


print(mix)


# In[53]:


mix[3]


# In[54]:


mix[-2]


# In[55]:


mix[:3]


# In[59]:


mix[3:]


# In[61]:


mix[2:4]


# In[64]:


mix[::2]


# In[65]:


mix[::-1]


# # Opertionss on list

# In[66]:


z=(0)*100
print(z)


# In[67]:


print(letter)


# In[68]:


print(stg)


# In[75]:


conc = letter + stg


# In[76]:


list1 = [10, 11, 12, 13, 14] 
list2 = [20, 30, 42] 


res = list1 + list2 


print ("Concatenated list:\n" + str(res))


# In[77]:


conc= letter +stg


# In[78]:


var = list("shivam prajapati")
print(var)


# In[79]:


print(num)


# In[80]:


one,*other = num
print(one)
print(other)


# # Method in list

# In[81]:


print(num)


# In[82]:


num.append(6)
print(num)


# In[83]:


num.extend(stg)
print(stg)
print(num)


# In[84]:


num.insert(5,"pankaj")
print(num)


# In[88]:


num.insert(6,"suneet yadav")
print(num)


# 

# In[89]:


num.remove("ankit")
print(num)


# In[90]:


var1=['b','f','a','q','r']
var1.sort()
print(var1)


# # Built Function with list

# In[91]:


x = [93,23,66,77,88]
len(x)


# In[92]:


min(x)


# In[93]:


max(x)


# In[94]:


sum(x)


# In[95]:


sum(x)/len(x)


# In[ ]:




