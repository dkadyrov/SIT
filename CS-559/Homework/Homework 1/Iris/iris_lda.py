import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

iris = datasets.load_iris()

X = iris.data
y = iris.target
names = iris.target_names

lda = LDA(n_components=2)
model = lda.fit(X, y).transform(X)

plt.figure()
for i, name in zip([0, 1, 2], names):
    plt.scatter(model[y == i, 0], model[y == i, 1], label=name)
plt.legend()
plt.xlabel("LD1")
plt.ylabel("LD2")
plt.show()
