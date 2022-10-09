#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


titanic_df = sns.load_dataset("titanic")


# In[3]:


titanic_df


# In[5]:


sns.scatterplot(x ="age",y="fare",data = titanic_df,hue="sex")


# In[9]:


sns.scatterplot(x ="age",y="fare",data = titanic_df,hue="sex",style="who",)
plt.show()


# In[11]:


plt.figure(figsize=(16,9))
sns.scatterplot(x ="age",y="fare",data = titanic_df,hue="sex",style="who",size="who",sizes=(100,400))
plt.show()


# In[16]:


plt.figure(figsize =(16,9))
sns.scatterplot(x ="who",y="fare",data = titanic_df,hue="alive",style="alive",size="who",sizes=(100,400))
plt.show()


# In[17]:


plt.figure(figsize =(16,9))
sns.scatterplot(x ="who",y="fare",data = titanic_df,hue="alive",
                style="alive",size="who",sizes=(100,400), palette="inferno_r",alpha=0.7,
)
plt.show()


# In[28]:


plt.figure(figsize =(16,9))
sns.scatterplot(x ="age",y ="fare",data=titanic_df)
sns.lineplot(x= "age",y= "fare",data=titanic_df)
sns.barplot(x= "age",y="fare",data=titanic_df)
plt.show()


# In[ ]:




