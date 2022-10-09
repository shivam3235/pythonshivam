#!/usr/bin/env python
# coding: utf-8

# # Pyhton seaborn part 3 and 4
# # mHow to draw Seaborn Histogram / Seborn Distplot

# In[23]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import random
from scipy.stats import norm


# In[7]:


m1_student_age= np.random.randint(18,45,(100))
pt_student_age= np.random.randint(15,40,(100))


# In[8]:


print(m1_student_age)
print(pt_student_age)


# In[10]:


tips_df = sns.load_dataset("tips")
tips_df


# In[12]:


sns.distplot(tips_df["size"])
plt.show()


# In[13]:


sns.distplot(tips_df["tip"])
plt.show()


# In[14]:


sns.distplot(tips_df["total_bill"])
plt.show()


# In[16]:


sns.distplot(tips_df["total_bill"],bins=100)
plt.show()


# In[18]:


sns.distplot(tips_df["total_bill"],hist= False)
plt.show()


# In[19]:


sns.distplot(tips_df["total_bill"],kde=False)
plt.show()


# In[20]:


sns.distplot(tips_df["total_bill"],rug=True)
plt.show()


# In[26]:


sns.distplot(tips_df["total_bill"],fit=norm,kit=False)
plt.show()


# In[28]:


sns.distplot(tips_df["total_bill"],color="r")
plt.show()


# In[29]:


sns.distplot(tips_df["total_bill"],vertical=True)
plt.show()


# In[30]:


sns.distplot(tips_df["total_bill"],norm_hist=True,)
plt.show()


# In[32]:


sns.distplot(tips_df["total_bill"],axlabel="Total Bill",)
plt.show()


# In[34]:


sns.distplot(tips_df["total_bill"],label="Total Bill",)
plt.show()


# In[35]:


sns.distplot(tips_df["total_bill"],label="Total Bill",)
plt.legend()
plt.show()


# In[36]:


sns.distplot(tips_df["total_bill"],label="Total Bill",)
plt.title("Histogram of total Bill")
plt.legend()
plt.show()


# In[38]:


plt.figure(figsize=(16,9))
sns.set()
sns.distplot(tips_df["total_bill"],label="Total Bill",)
plt.title("Histogram of total Bill")
plt.legend()
plt.show()


# In[39]:


tips_df.total_bill.sort_values()


# In[43]:


bins = [5,10,15,20,25,30,35,40,45,50,55]
plt.figure(figsize=(16,9))
sns.set()
sns.distplot(tips_df["total_bill"],bins=bins,)
plt.xticks(bins)

plt.title("Histogram of total Bill")
plt.show()


# In[48]:


plt.figure(figsize=(16,9))
sns.set()
sns.distplot(tips_df["total_bill"],hist_kws={"color":'#DC143C','edgecolor':'#aaff00','linewidth':5,'linestyle':'--'},)
plt.show()


# In[49]:


plt.figure(figsize=(16,9))
sns.set()
sns.distplot(tips_df["total_bill"],hist_kws={"color":'#DC143C',},)
plt.show()


# In[50]:


plt.figure(figsize=(16,9))
sns.set()
sns.distplot(tips_df["total_bill"],hist_kws={"color":'#DC143C','edgecolor':'#aaff00'},)
plt.show()


# In[51]:


plt.figure(figsize=(16,9))
sns.set()
sns.distplot(tips_df["total_bill"],hist_kws={"color":'#DC143C','edgecolor':'#aaff00','linewidth': 5},)
plt.show()


# In[52]:


plt.figure(figsize=(16,9))
sns.set()
sns.distplot(tips_df["total_bill"],hist_kws={"color":'#DC143C','edgecolor':'#aaff00','linewidth': 5,'linestyle':'--'},)
plt.show()


# In[53]:


plt.figure(figsize=(16,9))
sns.set()
sns.distplot(tips_df["total_bill"],hist_kws={"color":'#DC143C','edgecolor':'#aaff00','linewidth': 5,'linestyle':'--','alpha':0.9},)
plt.show()


# In[57]:


plt.figure(figsize=(16,9))
sns.set()
sns.distplot(tips_df["total_bill"],hist_kws={"color":'#DC143C','edgecolor':'#aaff00','linewidth': 5,'linestyle':'--','alpha':0.9},
kde_kws = {"color":'#8e00ce','linewidth': 8,'linestyle':'--','alpha':0.9},
            rug = True)

plt.show()


# In[58]:


plt.figure(figsize=(16,9))
sns.set()
sns.distplot(tips_df["total_bill"],hist_kws={"color":'#DC143C','edgecolor':'#aaff00','linewidth': 5,'linestyle':'--','alpha':0.9},
kde_kws = {"color":'#8e00ce','linewidth': 8,'linestyle':'--','alpha':0.9},
            rug = True,
            rug_kws ={"color":'#DC143C','edgecolor':'#aaff00','linewidth': 5,'linestyle':'--','alpha':0.9},)

plt.show()


# In[ ]:




