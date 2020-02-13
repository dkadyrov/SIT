import matplotlib.pyplot as plt

from sklearn import datasets, metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


iris = datasets.load_iris()

X = iris.data
y = iris.target
names = iris.target_names

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

k_range = range(1,51)

scores = {}
scores_list = []
print("K Value | Accuracy Score")
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)
    scores[k] = metrics.accuracy_score(y_test, pred)
    scores_list.append(scores[k])
    print("%i | %f"%(k, scores[k]))

plt.figure()
plt.plot(k_range, scores_list)
plt.title("Misclassification Rate")
plt.xlabel("KNN K Value")
plt.ylabel("Accuracy")
plt.show()
