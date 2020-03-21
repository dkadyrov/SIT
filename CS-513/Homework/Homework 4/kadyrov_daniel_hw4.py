# Course: CS 513B 
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Homework #4 Naive Bayes

import csv
from sklearn.naive_bayes import GaussianNB, CategoricalNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

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

# Split data into Training and Test
X_train, X_test, y_train, y_test = train_test_split(attributes, Class, test_size=0.30)

# Perform Naive Bayes using CategoricalNB
nb = CategoricalNB()
nb.fit(X_train, y_train)

y_pred = nb.predict(X_test)

# Evaluate Model
print("Accuracy (Categorical):",metrics.accuracy_score(y_test, y_pred))

# Perform Naive Bayes using GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)

# Evaluate Model
print("Accuracy (Gaussian):",metrics.accuracy_score(y_test, y_pred))
