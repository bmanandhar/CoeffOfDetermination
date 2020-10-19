#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[170]:


bills_and_tips = dict()         #an empty dict for bill and tip amounts
bills = [34,108,64,88,99,51]    #bill amounts
tips = [5,17,11,8,14,5]         #tip amounts
bills_and_tips['bills'] = bills
bills_and_tips['tips'] = tips
columns = ['bills', 'bills_dev', 'bills_dev_sqr', 'tips', 
            'tips_dev', 'tips_dev_sqr', 'devs_prod', 'tips_pred', 
            'obs_pred_diff', 'diff_sqr']


# In[39]:


# get_ipython().run_cell_magic('HTML', '', '<style type="text/css">\ntable.dataframe td, table.dataframe th {\n    border: 1px  black solid !important;\n  color: black !important;\n}\n</style>')


# In[171]:


df = pd.DataFrame(columns=columns)


# In[179]:


df.bills = bills
df.bills_dev = df.bills - np.mean(df.bills)    #bill amount deviation from mean
df.bills_dev_sqr = df.bills_dev**2             #square of dev


# In[181]:


df.tips = tips
df.tips_dev = df.tips - np.mean(df.tips)       #tip amount deviation from mean
df.tips_dev_sqr = df.tips_dev**2               #square of dev


# In[185]:


df.devs_prod = df.bills_dev*df.tips_dev        #product of bills_dev and tips_dev


# In[232]:


slope = round(sum(df.devs_prod)/sum(df.bills_dev_sqr), 4) 
intercept = round(slope*np.mean(df.bills) - np.mean(df.tips), 4)    #point where the st line meets at y-axis
df.tips_pred = slope*df.bills - intercept     #predicted tip amount
df.obs_pred_diff = tips - df.tips_pred        #diff between observed and predicted tip amounts
df.diff_sqr = df.obs_pred_diff**2


# In[233]:


df


# In[234]:


sse = round(sum(df.diff_sqr), 4)   #sum of suared errors
sst = sum(df.tips_dev_sqr)         
ssr = sst - sse                    #sum of squared errors due to regression
r2 = round(ssr/sst, 4)             #coeff of determination
r2                                 

#Graphs:

# %matplotlib inline

x = df.bills
y = df.tips
plt.plot(x,y,'o',label='Observed Tips', color='green')
plt.legend(loc='upper left')

x = df.bills
y = df.tips_pred
plt.plot(x,y,'o',label='Predicted Tips', color='purple')
plt.legend(loc='upper left')

m, b = 0, 10.0 #slope & intercept for mean-tips and customer nos
plt.plot(x, x*m+b, label='mean of observed tips')
plt.legend(loc='upper left')

x = np.linspace(30,115,100)
y=0.1462*x-0.8188                  
plt.plot(x, y, '-r', label='y=0.1462*x-0.8188')
plt.title('Graph of y=0.1462*x-0.8188')
plt.xlabel('Bill Amounts', color='#1C2833')
plt.ylabel('Tip Amounts', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()


# In[ ]:




