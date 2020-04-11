# Course: CS 513B
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Midterm - Problem 7

import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

# Read Data
with open('COVID19_v3.csv', newline='') as csvfile:
    next(csvfile)
    reader = csv.reader(csvfile)
    age, exposure, marital, cases, months, Infected = [], [], [], [], [], []

    for row in reader:
        # Clean data, Ignoring Rows with NA
        try:
            age.append(float(row[1]))
            exposure.append(float(row[2]))
            marital.append(row[3])
            cases.append(float(row[4]))
            months.append(float(row[5]))
            Infected.append(row[-1])
        except:
            pass

# Discretize the “MonthAtHospital” into “less than 6 months” and “6 or more months”
months_dis = []
for month in months:
    if month < 6: 
        months_dis.append(0)
    else: 
        months_dis.append(1)

# Discretize the age into “less than 35”, “35 to 50” and “51 or over”
age_dis = []
for a in age: 
    if a < 35: 
        age_dis.append(0)
    elif a >= 35 and a <= 50: 
        age_dis.append(1)
    else: 
        age_dis.append(2)

# Discretize marital
marital_dis = []
for marriage in marital: 
    if marriage == "Single": 
        marital_dis.append(0)
    elif marriage == "Married":
        marital_dis.append(1)
    else:
        marital_dis.append(2)

# Combine Attributes
attributes = [] 
for i in range(len(Infected)): 
    attributes.append(
        [age_dis[i], exposure[i], marital_dis[i], cases[i], months_dis[i]])

# Split data into Training and Test
X_train, X_test, y_train, y_test = train_test_split(
    attributes, Infected, test_size=0.30)

# KNN Classifier 
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Evaluate Model
print("Accuracy (CART):", metrics.accuracy_score(y_test, y_pred))
