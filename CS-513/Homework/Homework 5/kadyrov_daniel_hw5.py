# Course: CS 513B
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Homework #5 DTree

# Section 5.2 
import csv
from sklearn import tree
from sklearn import metrics
from sklearn.model_selection import train_test_split

# Read Data
with open('breast-cancer-wisconsin.data.csv', newline='') as csvfile:
    next(csvfile)
    reader = csv.reader(csvfile)
    Class = []
    attributes = []

    for row in reader:

        # Clean data, Ignoring Rows with NA
        try:
            attributes.append([float(i) for i in row[1:-1]])
            Class.append(float(row[-1]))
        except:
            pass

X_train, X_test, y_train, y_test = train_test_split(attributes, Class, test_size=0.30)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# Evaluate Model
print("Accuracy (CART):", metrics.accuracy_score(y_test, y_pred))
