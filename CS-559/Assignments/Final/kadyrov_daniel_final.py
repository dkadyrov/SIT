# Daniel Kadyrov
# CS 559 Final Exam

#%%
import pandas as pd 
import numpy as np

train = pd.read_csv("train.csv")
train = train.drop(columns=["Id"])

saleprice = pd.read_csv("SalePrice_File.csv")
# %%
# Part 1A
rows = train.shape[0]
cols = train.shape[1]
print("The dataset has {} rows".format(rows))
print("The dataset has {} features".format(cols))

# %%
# Part 1B
numeric = train._get_numeric_data().shape[1]
categorical = train.shape[1] - numeric

print("The dataset has {} categorical features".format(categorical))
print("The dataset has {} numerical features".format(numeric))

print("Categorical/String data can be converted to numerical through Encoding")

# %%
# Part 2a 

# Isn't part a and b asking the same question? What is 3 of total row mean? I do not understand the wording of this question

# %%
# Part 3b
# Eliminating columns/features with NA 

train['MasVnrArea'] = train["MasVnrArea"].fillna(method="ffill")
train['LotFrontage'] = train["LotFrontage"].fillna(method="ffill")
train['GarageYrBlt'] = train["GarageYrBlt"].fillna(method="ffill")

null = train.isnull().sum().sort_values(ascending=False)
print("Dropping columns {} because of NA".format(null.loc[null >0].index.tolist()))
# Dropping other columns and features with NA
train = train.dropna(axis=1)
train.shape

# %%
# Convert Categorical/String data to Numerical Through Encoding
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

categorical_feature_mask = train.dtypes == object
categorical_columns = train.columns[categorical_feature_mask].tolist()

train[categorical_columns] = train[categorical_columns].apply(lambda col: le.fit_transform(col))

train
# %%
# Correlation Between Variables and Sale Price
#Part 3b
correlation = train.corrwith(train["SalePrice"]) #.sort_values(ascending=False)
corr_over_05 = correlation.loc[correlation >= 0.5]
corr_over_05.sort_values(ascending=False)


# %%
# Part 3b Continued
corr_under_05 = correlation.loc[correlation <= 0.5]
corr_under_05.sort_values(ascending=False)

# %%
print("Features like {} can be removed to make it 40 features".format(corr_under_05.head(21).index.tolist()))

# %%
# Part 3c Done in earlier steps above

# %%
# Part 3d: Feature Selection using Random Forest Classifier 
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

x = train.drop("SalePrice", axis=1)
y = train["SalePrice"]

sel = SelectFromModel(RandomForestClassifier())
sel.fit(x, y)

#%%
selected_features = x.columns[(sel.get_support())]
selected_features
len(selected_features)

# %%
# Part 3C
x = train[selected_features]
x.head(10)

# Part D
# I used Random Forest to make a selection of features.

#%% 
# Part 4A
# Create training and testing datasets
from sklearn.model_selection import train_test_split 

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Linear Regression Ridge Classifier
from sklearn.linear_model import RidgeClassifier
from sklearn import metrics

regressor = RidgeClassifier()  
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

lin_error = np.sqrt(metrics.mean_squared_error(y_test, y_pred))

print('Root Mean Squared Error: {}'.format(lin_error))

# %%
# Part 4B with Ada Boost
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

clf = AdaBoostClassifier(DecisionTreeClassifier(), random_state=7)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

clf_error = np.sqrt(metrics.mean_squared_error(y_test, y_pred))

print('Root Mean Squared Error: {}'.format(clf_error))

# %%
# Part 4C with Combined 
from sklearn.ensemble import VotingClassifier

estimators = [('linear', regressor), ('gradient', clf)]
ensemble = VotingClassifier(estimators, voting='hard')

#fit model to training data
ensemble.fit(X_train, y_train)
#test our model on the test data
y_pred = ensemble.predict(X_test)

ensemble_error = np.sqrt(metrics.mean_squared_error(y_test, y_pred))

print('Root Mean Squared Error: {}'.format(ensemble_error))
# %%

print("AdaBoost Classifier performed the best")
# %%
# Part 5 
# Prepare Test Data
test = pd.read_csv("test.csv")
test = test.drop(columns = ["Id"])
test['MasVnrArea'] = test["MasVnrArea"].fillna(method="ffill")
test['LotFrontage'] = test["LotFrontage"].fillna(method="ffill")
test['GarageYrBlt'] = test["GarageYrBlt"].fillna(method="ffill")
test = test.dropna(axis=1)

categorical_feature_mask = test.dtypes == object
categorical_columns = test.columns[categorical_feature_mask].tolist()

test[categorical_columns] = test[categorical_columns].apply(lambda col: le.fit_transform(col))

# The columns of the test and training data are different so an intersection is created
common_columns = test.columns.intersection(x.columns)
x = x[common_columns]
test = test[common_columns]

clf = AdaBoostClassifier(DecisionTreeClassifier(), random_state=7)
clf.fit(x, y)
y_pred = clf.predict(test)

# %%
#Part 5a
y_actual = pd.read_csv("SalePrice_File.csv")

final_result = np.sqrt(metrics.mean_squared_error(y_actual["SalePrice"], y_pred))

y_actual = y_actual["SalePrice"].values
# %%
count = 0
for i in range(len(y_pred)):
    if abs(y_pred[i] - y_actual[i]) < final_result: 
        count += 1

print(count)
