# Daniel Kadyrov

#%%
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
from mlxtend.data import loadlocal_mnist


X_train, y_train = loadlocal_mnist(
    images_path='data/MNIST/train-images.idx3-ubyte',
    labels_path='data/MNIST/train-labels.idx1-ubyte'
)

x_test, y_test = loadlocal_mnist(
    images_path='data/MNIST/t10k-images.idx3-ubyte',
    labels_path='data/MNIST/t10k-labels.idx1-ubyte'
)

X_train = X_train.reshape(len(X_train), -1)
X_train = X_train.astype(float) / 255.


# %%
kmeans = KMeans(n_clusters=10, random_state=0).fit(X_train)

#%%

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1])
plt.show()

# # kmeans = KMeans(n_clusters=10, init='k-means++', random_state=42)
# # y_kmeans = kmeans.fit_predict(X_train)

# # %%
# nn = NearestNeighbors(n_neighbors=10, algorithm='ball_tree')

# nn.fit(X_train)

# # %% 
# # distances, indices = nn.kneighbors(X_train)
# # %%

# plt.scatter(nn.)


# # %%
# import numpy as np

# h = .02

# x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
# y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
#                         np.arange(y_min, y_max, h))
# Z = nn.predict(np.c_[xx.ravel(), yy.ravel()])


# # %%


# %%
