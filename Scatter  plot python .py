#!/usr/bin/env python
# coding: utf-8

# # Scatter plot

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd


# In[5]:


df_google_play_stor_app = pd.read_csv("F:\\machin\DataSet\googleplaystore.csv",nrows=1000)
df_google_play_stor_app.shape


# In[6]:


df_google_play_stor_app = pd.read_csv("F:\\machin\DataSet\googleplaystore.csv",nrows=1000)


# In[7]:


df_google_play_stor_app


# In[11]:


x = df_google_play_stor_app["Rating"]
y = df_google_play_stor_app["Reviews"]


# In[12]:


plt.scatter(x,y)
plt.show()


# In[13]:


plt.scatter(x,y)
plt.title("Google play store scatter plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# In[15]:


plt.figure(figsize= (16,9))
plt.scatter(x,y,c="g")
plt.title("Google play store scatter plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# In[18]:


plt.figure(figsize= (16,9))
plt.scatter(x,y,c="g",marker="*")
plt.title("Google play store scatter plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# In[19]:


plt.figure(figsize= (16,9))
plt.scatter(x,y,c="g",marker="*",s=100)
plt.title("Google play store scatter plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# In[22]:


plt.figure(figsize= (16,9))
plt.scatter(x,y,c="g",marker="*",s=100,alpha=0.5)
plt.title("Google play store scatter plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# In[23]:


plt.figure(figsize= (16,9))
plt.scatter(x,y,c="g",marker="*",s=100,alpha=0.5,linewidth=10)
plt.title("Google play store scatter plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# In[24]:


plt.figure(figsize= (16,9))
plt.scatter(x,y,c="g",marker="*",s=100,alpha=0.5,linewidth=10,edgecolor="b")
plt.title("Google play store scatter plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# In[27]:


plt.figure(figsize= (16,9))
plt.scatter(x,y,c="g",marker="*",s=100,alpha=0.5,linewidth=10)
plt.title("Google play store scatter plot")
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# In[30]:


plt.figure(figsize= (16,9))

plt.scatter(x,y,c="g",marker="*",s=100,alpha=0.5,linewidth=10,edgecolor="b")

plt.scatter(x,df_google_play_stor_app["Install"],c="y",marker="o",s=100,alpha=0.5,linewidth=10 ,edgecolor="r")
plt.title("Google play store scatter plot")
plt.xlabel("Rating")
plt.ylabel("Install")
plt.show()


# In[ ]:





# In[ ]:




