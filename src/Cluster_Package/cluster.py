#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import liberary 
from sklearn.preprocessing import StandardScaler 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering 
from scipy.cluster import hierarchy 
from scipy.spatial import distance_matrix 
get_ipython().run_line_magic('matplotlib', 'inline')

import os
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv('USWeather.txt') #read data
df.head() #Return the first 5 rows of the data.


# In[3]:


df.info() #print a summary of a Data(index dtype, column dtypes, non-null values and memory usage)


# In[6]:


X = df.drop(['date', 'actual_mean_temp'], axis=1)
sns.pairplot(df) # Print data in pairplot


# In[19]:


# The above figure does show few clusters of the data and the below code allow us to select the cluster
# when there is a significant change in inertia. 
clusters = []

for i in range(1, 11):
    km = KMeans(n_clusters=i).fit(X)
    clusters.append(km.inertia_)
    
fig, ax = plt.subplots(figsize=(12, 8))
sns.lineplot(x=list(range(1, 11)), y=clusters, ax=ax)
ax.set_title('Searching for Elbow')
ax.set_xlabel('Clusters')
ax.set_ylabel('Inertia')

# Annotate red arrow
ax.annotate('Possible Elbow Point Cluster=3', xy=(3, 800000), xytext=(3, 1000000), xycoords='data',          
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='red', lw=2))

ax.annotate('Possible Elbow Point Cluster=5', xy=(5, 550000), xytext=(5, 800000), xycoords='data',          
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='red', lw=2))

plt.show()


# In[20]:


# 5 cluster using K-means
km3 = KMeans(n_clusters=5).fit(X)

X['Labels'] = km3.labels_
plt.figure(figsize=(12, 8))
sns.scatterplot(X['actual_max_temp'], X['record_max_temp_year'], hue=X['Labels'], 
                palette=sns.color_palette('hls', 5))
plt.title('KMeans with 5 Clusters')
plt.show()


# In[21]:


fig = plt.figure(figsize=(20,8)) # plot the figure of with 5 clusters
ax = fig.add_subplot(121)
sns.swarmplot(x='Labels', y='actual_max_temp', data=X, ax=ax)
ax.set_title('Labels According to Actual Max Temp')

ax = fig.add_subplot(122)
sns.swarmplot(x='Labels', y='record_max_temp_year', data=X, ax=ax)
ax.set_title('Labels According to Record max Temp Year History')

plt.show()


# In[24]:


# 3 clusters using Agglomerative Hierarchical Clustering
# Dendrogram Associated for the Agglomerative Hierarchical Clustering with average linkage
agglom = AgglomerativeClustering(n_clusters=3, linkage='average').fit(X)

X['Labels'] = agglom.labels_
plt.figure(figsize=(12, 8))
sns.scatterplot(X['actual_max_temp'], X['record_max_temp_year'], hue=X['Labels'], 
                palette=sns.color_palette('hls', 3))
plt.title('Agglomerative with 3 Clusters')
plt.show()


# In[25]:


#plotting the dendrogram hierachy 
dist = distance_matrix(X, X)
Z = hierarchy.linkage(dist, 'average')
plt.figure(figsize=(18, 50))
dendro = hierarchy.dendrogram(Z, leaf_rotation=0, leaf_font_size=12, orientation='right')

