#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split


# In[8]:


df= pd.read_csv(r"E:\Personal\University\7th Semester\FYP\Dataset\Dataset\cryptojacking.csv");
df =df.select_dtypes(exclude=['object'])
df =df.dropna()
x_data=df;
y=x_data['target'];
x=(x_data-np.min(x_data))/(np.max(x_data)-np.min(x_data)).values
x.drop("cpu_steal",axis=1,inplace=True);
x.drop("target",axis=1,inplace=True)
x.info()


# In[9]:


filename = 'finalized_model.sav'
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42);
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(x_test, y_test)
print(result)


# In[ ]:




