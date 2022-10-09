#!/usr/bin/env python
# coding: utf-8

# # Seaborn part 5 and 6

# In[ ]:


# How to draw Seaborn barplot bar graph?


# In[7]:


import seaborn as sns
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt


# In[3]:


tips_df = sns.load_dataset("tips")
tips_df


# In[4]:


sns.barplot()


# In[8]:


sns.barplot(x= tips_df.total_bill)
plt.show()


# In[9]:


sns.barplot(x= tips_df.day, y= tips_df.total_bill)
plt.show()


# In[11]:


plt.figure(figsize=(16,9))
sns.barplot(x= tips_df.day, y= tips_df.total_bill,hue = tips_df.sex)

plt.show()


# In[12]:


plt.figure(figsize=(16,9))
sns.barplot(x= 'day',y = 'total_bill',hue='sex',data = tips_df)

plt.show()


# In[13]:


plt.figure(figsize=(16,9))
order = ['Sun','Thur','Fri','Sat']
sns.barplot(x= 'day',y = 'total_bill',hue='sex',data = tips_df,order= order)

plt.sho()


# In[22]:


plt.figure(figsize=(15,8))
sns.barplot(x= 'day',y = 'total_bill',hue='sex',data = tips_df,estimator=np.max, )

plt.show()


# In[23]:


plt.figure(figsize=(15,8))
sns.barplot(x= 'day',y = 'total_bill',hue='sex',data = tips_df,estimator=np.mean, )

plt.show()


# In[24]:


plt.figure(figsize=(15,8))
sns.barplot(x= 'day',y = 'total_bill',hue='sex',data = tips_df,
            estimator=np.mean,n_boot =2 )

plt.show()


# In[28]:


plt.figure(figsize=(15,8))
sns.barplot(x= 'day',y = 'total_bill',hue='sex',data = tips_df,orient="v", )

plt.show()


# In[30]:


plt.figure(figsize=(15,8))
sns.barplot(y= 'day',x = 'total_bill',hue='sex',data = tips_df, )

plt.show()


# In[34]:


plt.figure(figsize=(15,9))
sns.barplot(x = 'total_bill',y='size',hue='sex',data = tips_df,orient="h")
plt.show()


# In[37]:


plt.figure(figsize=(15,9))
sns.barplot(x = 'day',y='total_bill',hue='sex',data = tips_df,color='r')
plt.show()


# In[38]:


plt.figure(figsize=(15,9))
sns.barplot(x = 'day',y='total_bill',hue='sex',data = tips_df,color='r',palette="hot")
plt.show()


# In[39]:


plt.figure(figsize=(15,9))
sns.barplot(x = 'day',y='total_bill',hue='sex',data = tips_df,color='r',palette="magma")
plt.show()


# In[41]:


plt.figure(figsize=(15,9))
sns.barplot(x = 'day',y='total_bill',hue='sex',data = tips_df,saturation=0.3)
plt.show()


# In[44]:


plt.figure(figsize=(15,9))
sns.barplot(x = 'day',y='total_bill',hue='sex',data = tips_df, errcolor='0.3',)
plt.show()


# In[45]:


plt.figure(figsize=(15,9))
sns.barplot(x = 'day',y='total_bill',hue='sex',data = tips_df, errwidth=12,)
plt.show()


# In[49]:


plt.figure(figsize=(15,9))
sns.barplot(x = 'day',y='total_bill',hue='sex',data = tips_df, capsize=0.1,)
plt.show()


# In[50]:


plt.figure(figsize=(15,9))
sns.barplot(x = 'day',y='total_bill',hue='sex',data = tips_df, dodge=False,)
plt.show()


# In[53]:


plt.figure(figsize=(15,9))
kwargs ={'alpha':0.9,'linestyle':':','linewidth':'5','edgecolor':'k'}
sns.barplot(x = 'day',y='total_bill',hue='sex',data = tips_df,**kwargs,)
plt.show()


# In[54]:


plt.figure(figsize=(15,9))
sns.set()
kwargs ={'alpha':0.9,'linestyle':':','linewidth':'5','edgecolor':'k'}
sns.barplot(x = 'day',y='total_bill',hue='sex',data = tips_df,**kwargs,)
plt.show()


# In[55]:


plt.figure(figsize=(15,9))
sns.set()
kwargs ={'alpha':0.9,'linestyle':':','linewidth':'5','edgecolor':'k'}
sns.barplot(x = 'day',y='total_bill',data = tips_df,**kwargs,)
plt.show()


# In[61]:


plt.figure(figsize=(15,9))
#sns.set()
#kwargs ={'alpha':0.9,'linestyle':':','linewidth':'5','edgecolor':'k'}
sns.barplot(x = 'day',y='total_bill',data = tips_df,alpha=0.9,linestyle='-.',edgecolor='g',linewidth = 3)
plt.show()


# In[62]:


ax = sns.barplot(x = 'day',y='total_bill',data = tips_df,alpha=0.9,
                 linestyle='-.',edgecolor='g',linewidth = 3)
ax.set(title="Bar plot of Tips DataFrame",
      xlabel= "Day",
      ylabel = "total_bill")
plt.show()


# In[63]:


plt.figure(figsize= (16,9))
ax = sns.barplot(x = 'day',y='total_bill',data = tips_df,alpha=0.9,
                 linestyle='-.',edgecolor='g',linewidth = 3)
ax.set(title="Bar plot of Tips DataFrame",
      xlabel= "Day",
      ylabel = "total_bill")
plt.show()


# In[65]:


plt.figure(figsize =(16,9))
ax = sns.barplot(x = 'day',y='total_bill',data = tips_df,alpha=0.9,
                 linestyle='-.',edgecolor='g',linewidth = 3)
ax.set(title="Bar plot of Tips DataFrame",
      xlabel= "Day",
      ylabel = "total_bill")
plt.show()


# In[74]:


plt.figure(figsize=(16,9))
sns.barplot(x = 'day',y='total_bill',data = tips_df,alpha=0.9,linestyle='-.',edgecolor='g',linewidth = 3,
plt.title("Barplot of Days and total_bill") 


# In[ ]:


()

