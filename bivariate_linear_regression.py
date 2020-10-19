#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[170]:


bills_and_tips = dict()
bills = [34,108,64,88,99,51]
tips = [5,17,11,8,14,5]
bills_and_tips['bills'] = bills
bills_and_tips['tips'] = tips
columns = ['bills', 'bills_dev', 'bills_dev_sqr', 'tips', 'tips_dev', 'tips_dev_sqr', 'devs_prod', 'tips_pred', 'obs_pred_diff', 'diff_sqr']


# In[39]:


get_ipython().run_cell_magic('HTML', '', '<style type="text/css">\ntable.dataframe td, table.dataframe th {\n    border: 1px  black solid !important;\n  color: black !important;\n}\n</style>')


# In[171]:


df = pd.DataFrame(columns=columns)


# In[179]:


df.bills = bills
df.bills_dev = df.bills - np.mean(df.bills)
df.bills_dev_sqr = df.bills_dev**2


# In[181]:


df.tips = tips
df.tips_dev = df.tips - np.mean(df.tips)
df.tips_dev_sqr = df.tips_dev**2


# In[185]:


df.devs_prod = df.bills_dev*df.tips_dev


# In[224]:


slope = round(sum(df.devs_prod)/sum(df.bills_dev_sqr), 4)
intercept = round(slope*np.mean(df.bills) - np.mean(df.tips), 4)
df.tips_pred = slope*df.bills - intercept
df.obs_pred_diff = tips - df.tips_pred
df.diff_sqr = df.obs_pred_diff**2

print(intercept, slope)


# In[225]:


df


# In[231]:


sse = round(sum(df.diff_sqr), 4)   #sum of suared errors
sst = sum(df.tips_dev_sqr)         
ssr = sst - sse                    #sum of squared errors due to regression
r2 = round(ssr/sst, 4)             #coeff of determination
r2                                 


# In[ ]:



