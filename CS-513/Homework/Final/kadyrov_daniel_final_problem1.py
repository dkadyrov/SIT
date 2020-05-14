# Course: CS 513B
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Final Exam Problem 1

#%%
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
import pandas as pd

data = pd.read_csv('Admission.csv')
X = data[["GRE", "GPA"]]

#%% 
# Perform Kmeans 

kmeans = KMeans(n_clusters=2, random_state=7)
kmeans.fit(X)

results = pd.DataFrame(data={
    "ADMIT": data["ADMIT"],
    "KMEANS": kmeans.labels_
})

results
# %%
# Perform Hierarchal Clustering through AgglomerativeClustering package

hcluster = AgglomerativeClustering(
    n_clusters=2, affinity='euclidean', linkage='ward')
hcluster.fit_predict(X)

results["HIERARCHICAL"] = hcluster.labels_

results[["ADMIT", "HIERARCHICAL"]] 