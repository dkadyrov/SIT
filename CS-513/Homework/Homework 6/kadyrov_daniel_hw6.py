# %%
import numpy as np
import pandas as pd


data = pd.read_csv("breast-cancer-wisconsin.data.csv")
x = data["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"]
y = data["Class"]
# %%
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1) # 70% training and 30% test
