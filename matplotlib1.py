#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[6]:


xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()


# In[10]:


X =[2,5,9,7,8]
Y=[10,5,8,4,2]
plt.plot(X,Y)
plt.show()


# In[11]:


plt.bar(X,Y)
plt.show()


# In[12]:


plt.scatter(X,Y)
plt.show()


# In[15]:


plt.hist(Y)
plt.show()


# In[29]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
plt.plot(days, temperature)
plt.title("Lucknow temperature")
plt.xlabel("days")
plt.ylabel("Temperature")
plt.show()


# In[31]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
plt.plot(days, temperature)
plt.axis([0,30,0,50])
plt.title("Lucknow temperature")
plt.xlabel("days")
plt.ylabel("Temperature")
plt.show()


# In[38]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
plt.plot(days, temperature,color="g",marker="o",linestyle=":",linewidth=3,markersize=10)
plt.title("Lucknow temperature")
plt.xlabel("days")
plt.ylabel("Temperature")
plt.show()


# In[48]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
plt.plot(days, temperature,"go--",linewidth=3,markersize=10,label="tem line")
plt.title("Lucknow temperature",fontsize=15)
plt.xlabel("days",fontsize=13)
plt.ylabel("Temperature",fontsize=13)
plt.legend(loc=4)
plt.show()


# In[55]:


from matplotlib import style
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
style.use("ggplot")
plt.plot(days, temperature,"mo--",linewidth=3,markersize=10,label="tem line")
plt.title("Lucknow temperature",fontsize=15)
plt.xlabel("days",fontsize=13)
plt.ylabel("Temperature",fontsize=13)
plt.legend(loc=4)
plt.grid(color='k', linestyle='-.', linewidth=2)
plt.show()


# In[58]:



days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
delhi_tem = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
mumbai_tem = [39,39.4,40,40.7,41,42.5,43.5,44,44.9,44,45,45.1,46,47,46]
 
plt.plot(days, delhi_tem, "mo--", linewidth = 3,
        markersize = 10, label = "Delhi tem")
 
plt.plot(days, mumbai_tem, "yo:", linewidth = 3,
        markersize = 10, label = "Mumbai tem}")
 
plt.title("Delhi  & Mumbai Temperature", fontsize=15)
plt.xlabel("days",fontsize=13)
plt.ylabel("temperature",fontsize=13)
plt.legend(loc = 4)
plt.show()


# In[ ]:




