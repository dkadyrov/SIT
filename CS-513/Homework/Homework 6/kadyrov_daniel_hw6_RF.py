# Course: CS 513B
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Homework #6 RF

# %%
# Import and Process Data
import numpy as np
import pandas as pd

data = pd.read_csv("breast-cancer-wisconsin.data.csv", na_values="?")
data = data.dropna()
x = data[["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"]]
y = data["Class"]

# %%
# Seperate Training and Test Data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1) # 70% training and 30% test

# %%
# 6.1 C5.0 Methodology through DecisionTreeClassfiier Package (CART)
from sklearn.tree import DecisionTreeClassifier 

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
dt.score(X_test, y_test)
# %%
# 6.2 Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf.fit(X_train, y_train)
rf.score(X_test, y_test)

# %%
# Identify Important Features
feature_imp = pd.Series(rf.feature_importances_,index=x.columns).sort_values(ascending=False)
print(feature_imp)

# %%
