#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import numpy as np
import random


# 

# In[20]:


ml_student_age = np.random.randint(18,45,(100))
py_stydent_age = np.random.randint(15,40,(100))


# In[21]:


print(ml_student_age)
print(py_stydent_age)


# In[25]:


bins = [15,20,25,30,35,40,45]
plt.hist(ml_student_age,bins,rwidth=0.8)
plt.title("Machine Learing student")
plt.xlabel("student age catgeory")
plt.ylabel("No student age")
plt.show()


# In[27]:


bins = [15,20,25,30,35,40,45]
plt.hist(ml_student_age,bins,rwidth=0.8,histtype="bar")
plt.title("Machine Learing student")
plt.xlabel("student age catgeory")
plt.ylabel("No student age")
plt.show()


# In[36]:


bins = [15,20,25,30,35,40,45]
plt.hist(ml_student_age,bins,rwidth=0.8,histtype="bar",orientation='vertical',color="r")
plt.title("Machine Learing student")
plt.xlabel("student age catgeory")
plt.ylabel("No student age")
plt.show()


# In[44]:


bins = [15,20,25,30,35,40,45]
plt.hist(ml_student_age,bins,rwidth=0.8,histtype="bar",orientation='horizontal',
    color="y",label="Ml Student")
plt.title("Machine Learing student")
plt.xlabel("student age catgeory")
plt.ylabel("No student age")
plt.legend()
plt.show


# In[51]:


bins = [15,20,25,30,35,40,45]
plt.hist([ml_student_age,py_stydent_age],bins,rwidth=0.8,histtype="bar",orientation='vertical',
    color=["m","y"],label=["Ml Student","py student"])
#plt.hist(py_stydent_age,bins,rwidth=0.8,histtype="bar",orientation='vertical',
 #   color="r",label="py Student")


plt.title("Machine Learing student")
plt.xlabel("student age catgeory")
plt.ylabel("No student age")
plt.legend()
plt.show


# In[ ]:




