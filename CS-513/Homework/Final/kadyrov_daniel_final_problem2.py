# Course: CS 513B
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Final Exam Problem 2

#%%
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv('Admission_cat.csv', na_values='?')

# Preprocess Category Values
data = data.apply(LabelEncoder().fit_transform)

# Seperate training and test data
X_train, X_test, y_train, y_test = train_test_split(data[['RANK', 'GPA', 'GRE']], data['ADMIT'], test_size=0.3, random_state=7)

#%%  
# Random Forest Classification

rf = RandomForestClassifier()
rf.fit(X_train, y_train)
score = rf.score(X_test, y_test)

print("The accuracy of the model is: {}".format(score))
