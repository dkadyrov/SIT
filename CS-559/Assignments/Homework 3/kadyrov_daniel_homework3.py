# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np

data = []

col1 = np.random.uniform(
    low=-1.5, 
    high=np.nextafter(1.5, np.inf), 
    size=(1100,)
)
col2 = np.random.uniform(
    low=-3.5, 
    high=np.nextafter(1.5, np.inf), 
    size=(1100,)
)

col3 = np.random.randint(
    low=1, 
    high=np.nextafter(4, np.inf), 
    size=(1100,)
)

for i in range(len(col1)): 
    data.append([col1[i], col2[i]])


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

kmeans = KMeans()
kmeans.set_params(n_clusters=10)
kmeans.fit(data)

plt.scatter(col1, col2, c=kmeans.labels_, alpha=0.8)
plt.scatter(kmeans.cluster_centers_, marker="+", s=1000, c=[0, 1, 2])
plt.show()


