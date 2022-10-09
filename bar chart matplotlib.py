#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style


# In[3]:


classes = ["Python","R","AI","ML","DS"]
class1_student = [30,10,20,25,10]
class2_student =[40,5,20,20,10]
class3_student =[35,5,30,35,15]


# In[5]:


plt.bar(classes,class1_student)
plt.show()


# In[6]:


plt.barh(classes,class1_student)
plt.show()


# In[7]:


plt.bar(classes,class1_student,width=0.2)
plt.show()


# In[8]:


plt.bar(classes,class1_student,width=0.2,align="edge")
plt.show()


# In[9]:


plt.bar(classes,class1_student,width=0.2,align="edge",color="y")
plt.show()


# In[10]:


plt.bar(classes,class1_student,width=0.2,align="edge",color="y",edgecolor="m")
plt.show()


# In[12]:


plt.bar(classes,class1_student,width=0.2,align="edge",color="y",edgecolor="m",
       linewidth=5)
plt.show()


# In[13]:


plt.bar(classes,class1_student,width=0.2,align="edge",color="y",edgecolor="m",
       linewidth=5,alpha=0.5)
plt.show()


# In[16]:


plt.bar(classes,class1_student,width=0.2,align="edge",color="y",edgecolor="m",
       linewidth=5,alpha=0.9)
plt.show()


# In[18]:


plt.bar(classes,class1_student,width=0.2,align="edge",color="y",edgecolor="m",
       linewidth=5,alpha=0.5, linestyle="--")
plt.show()


# In[26]:


plt.bar(classes,class1_student,width=0.6,align="edge",color="k",edgecolor="m",
       linewidth=5,alpha=0.5, linestyle="--")
plt.show()


# In[27]:


style.use("ggplot")
plt.bar(classes,class1_student,width=0.6,align="edge",color="k",edgecolor="m",
       linewidth=5,alpha=0.5, linestyle="--")
plt.show()


# In[29]:


style.use("ggplot")
plt.figure(figsize=(16,9))
plt.bar(classes,class1_student,width=0.6,align="edge",color="r",edgecolor="m",
       linewidth=5,alpha=0.5, linestyle="--")
plt.show()


# In[31]:


style.use("ggplot")
plt.barh(classes,class1_student,align="edge",color="k",edgecolor="m",
       linewidth=5,alpha=0.5, linestyle="--")
plt.show()


# In[39]:


style.use("ggplot")
plt.bar(classes,class1_student,width=0.6,align="edge",color="k",edgecolor="m",
       linewidth=5,alpha=0.5, linestyle="--")
plt.title("Bar char of IaIp Class",fontsize=18)
plt.xlabel("class",fontsize=15)
plt.ylabel("no of Students",fontsize=15)
plt.show()


# In[41]:


style.use("ggplot")
plt.bar(classes,class1_student,width=0.2,color="b",
       label="class 1 Student")
plt.bar(classes,class2_student,width=0.2,color="g",
       label="Class 2 Student")

plt.title("Bar char of IaIp Class",fontsize=18)
plt.xlabel("class",fontsize=15)
plt.ylabel("no of Students",fontsize=15)
plt.show()


# In[42]:


style.use("ggplot")
classes_index = np.arange(len(classes))
width=0.2
plt.bar(classes_index ,class1_student,width,color="b",
       label="class 1 Student")
plt.bar(classes_index ,class2_student,width,color="g",
       label="Class 2 Student")

plt.title("Bar char of IaIp Class",fontsize=18)
plt.xlabel("class",fontsize=15)
plt.ylabel("no of Students",fontsize=15)
plt.show()


# In[47]:


style.use("ggplot")
classes_index = np.arange(len(classes))
width=0.2
plt.bar(classes_index ,class1_student,width,color="b",
       label="class 1 Student")
plt.bar(classes_index+width ,class2_student,width,color="g",
       label="Class 2 Student")

plt.bar(classes_index+width+width,class3_student,width,color="y",
       label="Class 2 Student")
plt.xticks(classes_index+width,classes,rotation=20)

plt.title("Bar char of IaIp Class",fontsize=18)
plt.xlabel("class",fontsize=15)
plt.ylabel("no of Students",fontsize=15)
plt.show()


# In[50]:


style.use("ggplot")
classes_index = np.arange(len(classes))
width=0.2
plt.barh(classes_index ,class1_student,width,color="b",
       label="class 1 Student")
plt.barh(classes_index+width ,class2_student,width,color="g",
       label="Class 2 Student")

plt.barh(classes_index+width+width,class3_student,width,color="y",
       label="Class 3 Student")
plt.yticks(classes_index+width,classes,rotation=20)

plt.title("Bar char of IaIp Class",fontsize=18)
plt.ylabel("class",fontsize=15)
plt.xlabel("no of Students",fontsize=15)
plt.legend()
plt.show()


# In[ ]:




