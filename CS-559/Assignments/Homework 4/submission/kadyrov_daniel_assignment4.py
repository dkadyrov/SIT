# Daniel Kadyrov
# CS 559 - Machine Learning
# Homewowrk 4 
# Problem 1-2

#%%
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from mlxtend.data import loadlocal_mnist
import numpy as np
import pandas as pd
from PIL import Image

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

x_test = x_test.reshape(len(x_test), -1)
x_test = x_test.astype(float) / 255.

# %%
kmeans = KMeans(n_clusters=10, random_state=0).fit(X_train)

#%%
def cluster_labels(kmeans, true_labels):
    cluster_labels = {}

    for i in range(kmeans.n_clusters): 
        labels = []

        index = np.where(kmeans.labels_ == i) 

        labels.append(true_labels[index])

        if len(labels[0]) == 1: 
            count = np.bincount(labels[0])
        else: 
            counts = np.bincount(np.squeeze(labels))

        label = np.argmax(counts)
        if label in cluster_labels:
            cluster_labels[label].append(i)
        else: 
            cluster_labels[label] = [i]

    return cluster_labels

def data_labels(xlabels, cluster_labels): 
    predicted = np.zeros(len(xlabels)).astype(np.uint8)

    for i, label in enumerate(xlabels): 
        for k, v in cluster_labels.items(): 
            if label in v: 
                predicted[i] = k

    return predicted
#%%
clusters = cluster_labels(kmeans, y_train)
y_pred = kmeans.predict(x_test)
predicted_labels = data_labels(y_pred, clusters)

accuracy = pd.DataFrame({
    "kmeans": [accuracy_score(y_test, predicted_labels)]
})


# %%
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(x_test)

accuracy["lr"] = accuracy_score(y_test, y_pred)
 
# %%
from sklearn.svm import SVC

svc = SVC(gamma=0.001)
svc.fit(X_train, y_train)
y_pred = svc.predict(x_test)

accuracy["svc"] = accuracy_score(y_test, y_pred)

# %%
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
y_pred = dt.predict(x_test)

accuracy["dt"] = accuracy_score(y_test, y_pred)

# %% 
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)
y_pred = rfc.predict(x_test)

accuracy["rf"] = accuracy_score(y_test, y_pred)

# %%
with open('accuracy_part3.tex', 'w') as tf:
     tf.write(accuracy.to_latex(index=False))

# %%


# %%
import cv2
import os
import imageio
from PIL import Image

im = Image.open('data\Handwriting\IMG_20200508_112313.jpg').convert("L")

width, height = im.size

# x = np.array([])
y = np.array([])
x = []
for i in range(10):
    for j in range(5):
        y = np.append(y, [i+1]) #= np.append(y, [i+1])
        img = im.crop((i*width/10, (j)*height/5, (i+1)*width/10, (j+1)*height/5))

        img = img.resize((64, 64))
        # img = np.array(img)
        # img = img.reshape(1, 28, 28, 1)

        # x = np.append(x, [img])
        x.append(img)
        # x = np.append(x, [np.array(img).reshape(1,28,28,1)], axis=0)
        # x.append(np.array(img).reshape(1,28,28,1))
y = np.where(y==10, 0, y)

# x = [] ##np.array([])
# y = [] #np.array([])
# for file in os.listdir("data\Handwriting\Processed"):
    # y = np.append(y, file.split("_")[0])
    # y.append(file.split("_")[0])
#     # break
    # gray = cv2.imread(os.path.join("data\Handwriting\Processed", file), 0)
    # gray = cv2.resize(gray, (28, 28)).flatten() / 255.0
    # x = np.append(x, [gray])
   # im = cv2.imread(os.path.join("data\Handwriting\Processed", file), 0)
    # image = 
    
    # im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)
    # x.append(np.array([cv2.imread(os.path.join("data\Handwriting\Processed", file)))

# x /= 255
# clusters = cluster_labels(kmeans, y_train)
# %% 
y_pred = kmeans.predict(np.asarray(x)) #.reshape(-1, 1))
predicted_labels = data_labels(y_pred, clusters)

accuracy_hand = pd.DataFrame({
    "kmeans": [accuracy_score(y_test, predicted_labels)]
})

y_pred = lr.predict(x.reshape(-1, 1))
accuracy_hand["lr"] = accuracy_score(y, y_pred)

y_pred = svc.predict(x.reshape(-1, 1))
accuracy_hand["svc"] = accuracy_score(y, y_pred)

y_pred = dt.predict(x)
accuracy_hand["dt"] = accuracy_score(y, y_pred)

y_pred = rfc.predict(x)
accuracy_hand["rf"] = accuracy_score(y, y_pred)



# %%
