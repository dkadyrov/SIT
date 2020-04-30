Daniel Kadyrov

CS559 - Homework 3 

Question 4


```python
import pandas as pd

headers = ["f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"]
data_old = pd.read_csv("HW3_Q4_01_1.csv", names=headers)
```


```python
import numpy as np 

class kmeansalt:
    def __init__(self, n_clusters, max_iter=100, random_state=123): 
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state
    
    def initialize_centroids(self, X): 
        np.random.RandomState(self.random_state)
        random_idx = np.random.permutation(X.shape[0])
        centroids = X[random_idx[:self.n_clusters]]

        return centroids

    def compute_centroids(self, X, labels):
        centroids = np.zeros((self.n_clusters, X.shape[1]))
        for k in range(self.n_clusters):
            centroids[k, :] = np.mean(X[labels == k, :], axis=0)
        
        return centroids

    def compute_distance(self, X, centroids):
        distance = np.zeros((X.shape[0], self.n_clusters))
        for k in range(self.n_clusters):
            row_norm = np.linalg.norm(X - centroids[k, :], axis=1)
            distance[:, k] = np.square(row_norm)
        
        return distance

    def find_closest_cluster(self, distance):
        
        return np.argmin(distance, axis=1)

    def compute_sse(self, X, labels, centroids):
        distance = np.zeros(X.shape[0])
        for k in range(self.n_clusters):
            distance[labels == k] = np.linalg.norm(X[labels == k] - centroids[k], axis=1)
        
        return np.sum(np.square(distance))
    
    def fit(self, X):
        self.centroids = self.initialize_centroids(X)
        for i in range(self.max_iter):
            old_centroids = self.centroids
            distance = self.compute_distance(X, old_centroids)
            self.labels = self.find_closest_cluster(distance)
            self.centroids = self.compute_centroids(X, self.labels)
            if np.all(old_centroids == self.centroids):
                break
        self.error = self.compute_sse(X, self.labels, self.centroids)
    
    def predict(self, X):
        distance = self.compute_distance(X, old_centroids)

        return self.find_closest_cluster(distance)

    def cluster_variance(self): 
        unique_labels = np.unique(self.labels)
        cluster_size = []
        for label in unique_labels: 
            cluster_size.append(len(X[km.labels==label, 0]))

        return unique_labels, cluster_size    
```


```python
from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(data_old)

km = kmeansalt(n_clusters=6, max_iter=100)
km.fit(X)
cluster, size = km.cluster_variance()

import matplotlib.pyplot as plt

plt.bar(cluster, size)
plt.xlabel("Cluster Number")
plt.ylabel("Cluster Size")
plt.show()
```


![svg](kadyrov_daniel_homework3_Q4_files/kadyrov_daniel_homework3_Q4_3_0.svg)



```python
data_old["class"] = km.labels
data_old.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>f0</th>
      <th>f1</th>
      <th>f2</th>
      <th>f3</th>
      <th>f4</th>
      <th>f5</th>
      <th>f6</th>
      <th>f7</th>
      <th>f8</th>
      <th>class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>288</td>
      <td>4</td>
      <td>96</td>
      <td>56</td>
      <td>17</td>
      <td>49</td>
      <td>20.8</td>
      <td>0.340</td>
      <td>26</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>470</td>
      <td>1</td>
      <td>144</td>
      <td>82</td>
      <td>40</td>
      <td>0</td>
      <td>41.3</td>
      <td>0.607</td>
      <td>28</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>581</td>
      <td>6</td>
      <td>109</td>
      <td>60</td>
      <td>27</td>
      <td>0</td>
      <td>25.0</td>
      <td>0.206</td>
      <td>27</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>620</td>
      <td>2</td>
      <td>112</td>
      <td>86</td>
      <td>42</td>
      <td>160</td>
      <td>38.4</td>
      <td>0.246</td>
      <td>28</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>333</td>
      <td>12</td>
      <td>106</td>
      <td>80</td>
      <td>0</td>
      <td>0</td>
      <td>23.6</td>
      <td>0.137</td>
      <td>44</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(data_old[["f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"]], data_old["class"], test_size=.2)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(x_train, y_train)
lr.score(x_test, y_test)

```




    0.7739130434782608




```python
from sklearn.cluster import KMeans

X = StandardScaler().fit_transform(data_old[["f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"]])
kmeans = KMeans(n_clusters=6).fit(X)
unique_labels = np.unique(kmeans.labels_)
cluster_size = []
for label in unique_labels: 
    cluster_size.append(len(X[kmeans.labels_==label, 0]))

plt.bar(unique_labels, cluster_size)
plt.xlabel("Cluster Number")
plt.ylabel("Cluster Size")
plt.show()
```


![svg](kadyrov_daniel_homework3_Q4_files/kadyrov_daniel_homework3_Q4_6_0.svg)



```python
data_old["class"] = kmeans.labels_
data_old.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>f0</th>
      <th>f1</th>
      <th>f2</th>
      <th>f3</th>
      <th>f4</th>
      <th>f5</th>
      <th>f6</th>
      <th>f7</th>
      <th>f8</th>
      <th>class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>288</td>
      <td>4</td>
      <td>96</td>
      <td>56</td>
      <td>17</td>
      <td>49</td>
      <td>20.8</td>
      <td>0.340</td>
      <td>26</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>470</td>
      <td>1</td>
      <td>144</td>
      <td>82</td>
      <td>40</td>
      <td>0</td>
      <td>41.3</td>
      <td>0.607</td>
      <td>28</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>581</td>
      <td>6</td>
      <td>109</td>
      <td>60</td>
      <td>27</td>
      <td>0</td>
      <td>25.0</td>
      <td>0.206</td>
      <td>27</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>620</td>
      <td>2</td>
      <td>112</td>
      <td>86</td>
      <td>42</td>
      <td>160</td>
      <td>38.4</td>
      <td>0.246</td>
      <td>28</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>333</td>
      <td>12</td>
      <td>106</td>
      <td>80</td>
      <td>0</td>
      <td>0</td>
      <td>23.6</td>
      <td>0.137</td>
      <td>44</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
x_train, x_test, y_train, y_test = train_test_split(data_old[["f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"]], data_old["class"], test_size=.2)

lr = LogisticRegression()
lr.fit(x_train, y_train)
lr.score(x_test, y_test)
```




    0.8260869565217391




```python
headers = ["f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "class"]
data_new = pd.read_csv("HW3_Q4_1.csv", names=headers)
```


```python
from sklearn.metrics import accuracy_score

accuracy_score(data_new["class"], data_old["class"])
```




    0.08869565217391304




```python
unique_classes = np.unique(data_new["class"])
unique_classes
```




    array([0, 1])



My model was very poor. 


```python
x_train, x_test, y_train, y_test = train_test_split(data_new[["f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"]], data_new["class"], test_size=.2)

lr.fit(x_train, y_train)
lr_accuracy = lr.score(x_test, y_test)
lr_accuracy
```




    0.7478260869565218




```python
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(data_new[["f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"]], data_new["class"])
```




    RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                           criterion='gini', max_depth=None, max_features='auto',
                           max_leaf_nodes=None, max_samples=None,
                           min_impurity_decrease=0.0, min_impurity_split=None,
                           min_samples_leaf=1, min_samples_split=2,
                           min_weight_fraction_leaf=0.0, n_estimators=100,
                           n_jobs=None, oob_score=False, random_state=None,
                           verbose=0, warm_start=False)




```python
data_test = pd.read_csv("HW3_Q4_2.csv", skiprows=1, names=headers)
data_test["f0"] = data_test["f0"].astype(float)
data_test.head() 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>f0</th>
      <th>f1</th>
      <th>f2</th>
      <th>f3</th>
      <th>f4</th>
      <th>f5</th>
      <th>f6</th>
      <th>f7</th>
      <th>f8</th>
      <th>class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.0</td>
      <td>5</td>
      <td>116</td>
      <td>74</td>
      <td>0</td>
      <td>0</td>
      <td>25.6</td>
      <td>0.201</td>
      <td>30</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11.0</td>
      <td>10</td>
      <td>168</td>
      <td>74</td>
      <td>0</td>
      <td>0</td>
      <td>38.0</td>
      <td>0.537</td>
      <td>34</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14.0</td>
      <td>5</td>
      <td>166</td>
      <td>72</td>
      <td>19</td>
      <td>175</td>
      <td>25.8</td>
      <td>0.587</td>
      <td>51</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21.0</td>
      <td>8</td>
      <td>99</td>
      <td>84</td>
      <td>0</td>
      <td>0</td>
      <td>35.4</td>
      <td>0.388</td>
      <td>50</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.0</td>
      <td>11</td>
      <td>143</td>
      <td>94</td>
      <td>33</td>
      <td>146</td>
      <td>36.6</td>
      <td>0.254</td>
      <td>51</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
pred = rfc.predict(data_test[["f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"]])

rfc_accuracy = accuracy_score(data_test["class"], pred)

rfc_accuracy
```




    0.7552083333333334




```python
"Logistic Regression: {} \n Random Forest: {}".format(lr_accuracy, rfc_accuracy)
```




    'Logistic Regression: 0.7478260869565218 \n Random Forest: 0.7552083333333334'




```python
from sklearn.ensemble import GradientBoostingClassifier

gbc = GradientBoostingClassifier()
gbc.fit(data_new[["f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"]], data_new["class"])

pred = gbc.predict(data_test[["f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"]])

gbc_accuracy = accuracy_score(data_test["class"], pred)

gbc_accuracy
```




    0.7760416666666666




```python

```
