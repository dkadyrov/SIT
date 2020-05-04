# Course: CS 513B
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Homework #8 Clustering

# %%
import pandas as pd

data = pd.read_csv("wisc_bc_ContinuousVar.csv", na_values="?")
data = data.dropna()

#%%

data["diagnosis norm"] = data["diagnosis"].factorize()[0] #data["Class"].apply(lambda x: )
x = data.iloc[:,2:-1]

# %%
from sklearn.cluster import AgglomerativeClustering

cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
cluster.fit_predict(x)

# %%
from sklearn.metrics import accuracy_score

data["hclust"] = cluster.labels_

score = accuracy_score(data["predicted"], data["diagnosis norm"])
print(score)
data[data["diagnosis"], data["kmeans"]]
#%%
import matplotlib.pyplot as plt

# plt.plot(data["diagnosis norm"])
# plt.plot(data["predicted"])
plt.scatter(data["radius_mean"], data["texture_mean"], c=data["diagnosis norm"])
plt.show()

# %%
plt.scatter(data["radius_mean"], data["texture_mean"], c=data["hclust"])
plt.show()

# %%
# Section 8.2
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2)
kmeans.fit(x)
data["kmeans"] = kmeans.labels_.astype(int)

plt.scatter(data["radius_mean"], data["texture_mean"], c=data["kmeans"])
plt.show()

data[data["diagnosis"], data["kmeans"]]