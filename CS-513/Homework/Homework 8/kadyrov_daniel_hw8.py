# Course: CS 513B
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Homework #8 Clustering

# %%
# Import Dataset and drop rows with NaN
import pandas as pd

data = pd.read_csv("wisc_bc_ContinuousVar.csv", na_values="?")
data = data.dropna()

#%%
# Normalize Diagnosis data
data["diagnosis norm"], label = data["diagnosis"].factorize()
x = data.iloc[:,2:-1]

# %%
# Perform Hierarchal Clustering through AgglomerativeClustering package
from sklearn.cluster import AgglomerativeClustering

cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
cluster.fit_predict(x)

# %%
from sklearn.metrics import accuracy_score

data["hclust"] = label[cluster.labels_]

score = accuracy_score(data["hclust"], data["diagnosis"])
print(score)

# %%
# Tabulate the clustered rows against the “diagnosis” column
print(data[["diagnosis", "hclust"]])

# %%
# Section 8.2
# Using k-means, categorize the “wisc_bc_ContinuousVar.csv” data into two (2) clusters based on. All the features except the diagnosis column
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2)
kmeans.fit(x)
data["kmeans"] = label[kmeans.labels_]
score = accuracy_score(data["kmeans"], data["diagnosis"])
print(score)

# %%
# Tabulate the clustered rows against the “diagnosis” column
print(data[["diagnosis", "kmeans"]])
