#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB


# In[3]:


warnings.filterwarnings('ignore')


# In[4]:


df= pd.read_csv(r"E:\Personal\University\7th Semester\FYP\Dataset\Dataset\cryptojacking.csv");


# In[ ]:





# In[5]:


#Data Cleaning
'''Dropping the null objects in the dataset'''
df =df.select_dtypes(exclude=['object'])
df =df.dropna()


# In[6]:


df.info()


# In[7]:


'''Describing the data as a statistical form'''
normal = df.loc[df['target']==0,:]
normal.describe()


# In[8]:


abnormal = df.loc[df['target']==1,:]
abnormal.describe()


# In[9]:


#Feature Extraction
#KDE graph
#A kernel density estimate (KDE) plot is a method for visualizing the distribution of observations in a 
#dataset, analagous to a histogram. KDE represents the data using a continuous probability density curve in one or more dimensions.

features = df.columns[:-1]
plt.figure(figsize=(20,50))
i=1
for feature in features:
    plt.subplot(11,3,i)
    sns.kdeplot(normal[feature],shade=True)
    sns.kdeplot(abnormal[feature],shade=True)
    i=i+1
    plt.tight_layout()
plt.show()


# In[10]:


plt.figure(figsize=(20,50))
i=1
for feature in normal.columns:
    plt.subplot(11,3,i)
    plt.hist(normal[feature],bins=100)
    plt.hist(abnormal[feature],bins=100)
    plt.title(feature)
    i=i+1
plt.tight_layout()
plt.show()


# In[11]:


f, ax = plt.subplots(figsize=(18,18))
sns.heatmap(df.corr(), annot=True, linewidths=.5,cmap="Accent",fmt='.1f',ax=ax)
plt.title('Correlation Map')
plt.show()


# In[12]:


def ztest(feature):
    mean= normal[feature].mean()
    std=abnormal[feature].std()
    zScore = (abnormal[feature].mean()-mean)/(std/np.sqrt(sample_size))
    return zScore

columns=df.drop('target',axis=1).columns
normal = df[df.target==0]
abnormal=df[df.target==1]
sample_size=len(abnormal)
significant_features=[]
critical_value=2.58

for i in columns:
    z_value=ztest(i)
    
    if(abs(z_value)>= critical_value):
        print(i,"is statistically significant")
        significant_features.append(i)


# In[13]:


# Data Normalization
x_data=df;
y=x_data['target'];

x=(x_data-np.min(x_data))/(np.max(x_data)-np.min(x_data)).values


# In[14]:


x.drop("cpu_steal",axis=1,inplace=True);
x.drop("target",axis=1,inplace=True)
x.info()


# In[15]:


#Spliting the data 
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42);


# In[16]:


gb=GaussianNB();
gb.fit(x_train,y_train)
y_pred=gb.predict(x_test)
print(accuracy_score(y_test, y_pred))


# In[17]:


confusion_matrix(y_test, y_pred)
print("f1 score:",f1_score(y_test,y_pred),"\nPrecision:" ,precision_score(y_test,y_pred),"\nRecall:", recall_score(y_test,y_pred))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[37]:





# In[ ]:




