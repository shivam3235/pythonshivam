#!/usr/bin/env python
# coding: utf-8

# # python Seaborn part 1 and  2

# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[4]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
sns.lineplot(days,temperature)


# In[5]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
sns.lineplot(days,temperature)
sns.show()


# In[11]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
temp_df = pd.DataFrame({"days":days,"temperature":temperature})
sns.lineplot( x="days",y = "temperature",data=temp_df,)


# In[12]:


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
temp_df = pd.DataFrame({"days":days,"temperature":temperature})
sns.lineplot( x="days",y = "temperature",data=temp_df,)
plt.show()


# In[14]:


tips_df = sns.load_dataset("tips")
tips_df


# In[15]:


tips_df.shape


# In[16]:


sns.lineplot(x ="total_bill",y="tip",data=tips_df)
plt.show()


# In[22]:


sns.lineplot(x ="tip",y="total_bill",data=tips_df)
plt.show()


# In[23]:


sns.lineplot(x ="tip",y="size",data=tips_df)
plt.show()


# In[24]:


sns.lineplot(x ="size",y="total_bill",data=tips_df)
plt.show()


# In[25]:


sns.lineplot(x ="size",y="total_bill",data=tips_df,hue="sex")
plt.show()


# In[26]:


sns.lineplot(x ="size",y="total_bill",data=tips_df,hue="sex",style="sex")
plt.show()


# In[27]:


sns.lineplot(x ="size",y="total_bill",data=tips_df,hue="sex",style="sex",palette="Accent")
plt.show()


# In[31]:


sns.lineplot(x ="size",y="total_bill",data=tips_df,hue="sex",style="sex",
             palette="Accent",dashes=False)
plt.show()


# In[32]:


sns.lineplot(x ="size",y="total_bill",data=tips_df,hue="sex",style="sex",
             palette="hot",dashes=False,)
plt.show()


# In[37]:


sns.lineplot(x ="size",y="total_bill",data=tips_df,hue="sex",style="sex",
             palette="hot",dashes=False,markers = ["o","<"])
plt.show()


# In[40]:


sns.lineplot(x ="size",y="total_bill",data=tips_df,hue="sex",style="sex",
             palette="hot",dashes=False,markers = ["o","<"],legend='brief',)
plt.show()


# In[41]:


sns.lineplot(x ="size",y="total_bill",data=tips_df,hue="sex",style="sex",
             palette="hot",dashes=False,markers = ["o","<"],legend=False,)
plt.show()


# In[42]:


sns.lineplot(x ="size",y="total_bill",data=tips_df,hue="sex",style="sex",
             palette="hot",dashes=False,markers = ["o","<"],legend='brief',)
plt.xlabel("Size",fontsize=15)
plt.ylabel("Total Bill",fontsize= 15)
plt.show()


# In[45]:


sns.lineplot(x ="size",y="total_bill",data=tips_df,hue="sex",style="sex",
             palette="hot",dashes=False,markers = ["o","<"],legend='brief',)
plt.title("Line plot  ",fontsize= 20)
plt.xlabel("Size",fontsize=15)
plt.ylabel("Total Bill",fontsize= 15)
plt.show()


# In[46]:


sns.set(style="darkgrid")
sns.lineplot(x ="size",y="total_bill",data=tips_df,hue="sex",style="sex",
             palette="hot",dashes=False,markers = ["o","<"],legend='brief',)
plt.title("Line plot  ",fontsize= 20)
plt.xlabel("Size",fontsize=15)
plt.ylabel("Total Bill",fontsize= 15)
plt.show()


# In[48]:


plt.figure(figsize =(16,9))
sns.set(style="darkgrid")
sns.lineplot(x ="size",y="total_bill",data=tips_df,hue="sex",style="sex",
             palette="hot",dashes=False,markers = ["o","<"],legend='brief',)
plt.title("Line plot  ",fontsize= 20)
plt.xlabel("Size",fontsize=15)
plt.ylabel("Total Bill",fontsize= 15)
plt.show()


# In[49]:


plt.figure(figsize =(16,9))
sns.set(style="darkgrid")
sns.lineplot(x ="size",y="total_bill",data=tips_df,hue="day",style="day",
             palette="hot",dashes=False,markers = ["o","<",">","^"],legend='brief',)
plt.title("Line plot  ",fontsize= 20)
plt.xlabel("Size",fontsize=15)
plt.ylabel("Total Bill",fontsize= 15)
plt.show()


# In[ ]:




