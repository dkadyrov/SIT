import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from matplotlib import pyplot as plt

columns = ["sepal length", "sepal width",
           "petal length", "petal width", "class"]

data = pd.read_csv("iris/iris.data", header=None)

data.columns = columns

X = data[[columns[0], columns[1], columns[2], columns[3]]].values
y = data["class"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

lda = LDA(n_components=3).fit(X_train, y_train)

X_train = lda.fit_transform(X_train, y_train)
X_test = lda.transform(X_test)

plt.figure()
plt.scatter(X_train[0], y_train[0])
plt.show()

