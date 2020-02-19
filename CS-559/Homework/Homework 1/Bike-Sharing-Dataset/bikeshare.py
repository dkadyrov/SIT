import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso, BayesianRidge
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
import numpy as np

hour = pd.read_csv("hour.csv")
day = pd.read_csv("day.csv")

cnt_hour = hour["cnt"].values.reshape(-1, 1)
cnt_day = day["cnt"].values.reshape(-1, 1)

def make_graphs():
    for col in range(len(hour.columns)):
        if hour.columns[col] not in ["instant", "cnt", "dteday", "registered", "casual"]:
            plt.figure()
            plt.scatter(hour[hour.columns[col]].values.reshape(-1, 1), cnt_hour)
            plt.title("{} vs. Hourly Rider Count".format(hour.columns[col]))
            plt.xlabel("{}".format(hour.columns[col]))
            plt.ylabel("{}".format("Hourly Rider Count"))
            plt.savefig("images/hour_{}.png".format(hour.columns[col]))
            plt.clf()

    for col in range(len(day.columns)):
        if day.columns[col] not in ["instant", "cnt", "dteday", "registered", "casual"]:
            plt.figure()
            plt.scatter(day[day.columns[col]].values.reshape(-1, 1), cnt_day)
            plt.title("{} vs. Daily Rider Count".format(day.columns[col]))
            plt.xlabel("{}".format(day.columns[col]))
            plt.ylabel("{}".format("Daily Rider Count"))
            plt.savefig("images/day_{}.png".format(day.columns[col]))
            plt.clf()

# make_graphs()

day_temp = day["temp"].values.reshape(-1, 1) * 41

crossvalidation = KFold(n_splits=10)
linear = LinearRegression()
ridge = Ridge()
lasso = Lasso()
bayesian = BayesianRidge()

for train_index, test_index in crossvalidation.split(day_temp):
    X_train, X_test = day_temp[train_index], day_temp[test_index]
    y_train, y_test = cnt_day[train_index], cnt_day[test_index]
    linear.fit(X_train, y_train)
    ridge.fit(X_train, y_train)
    lasso.fit(X_train, y_train)
    bayesian.fit(X_train, y_train)

linear_pred = linear.predict(X_test)
ridge_pred = ridge.predict(X_test)
lasso_pred = lasso.predict(X_test)
bayesian_pred = bayesian.predict(X_test)

mse_linear = mean_squared_error(y_test, linear_pred)
mse_ridge = mean_squared_error(y_test, ridge_pred)
mse_lasso = mean_squared_error(y_test, lasso_pred)
mse_bayesian = mean_squared_error(y_test, bayesian_pred)

plt.figure()
plt.scatter(day_temp, cnt_day)
plt.plot(X_test, linear_pred, color="red")
plt.title("Linear: Day Temperature vs. Rider Count")
plt.xlabel("Temperature [deg C]")
plt.ylabel("Rider Count")
plt.savefig("images/linear.png")
plt.clf()

plt.figure()
plt.scatter(day_temp, cnt_day)
plt.plot(X_test, ridge_pred, color="red")
plt.title("Ridge: Day Temperature vs. Rider Count")
plt.xlabel("Temperature [deg C]")
plt.ylabel("Rider Count")
plt.savefig("images/ridge.png")
plt.clf()

plt.figure()
plt.scatter(day_temp, cnt_day)
plt.plot(X_test, lasso_pred, color="red")
plt.title("Lasso: Day Temperature vs. Rider Count")
plt.xlabel("Temperature [deg C]")
plt.ylabel("Rider Count")
plt.savefig("images/lasso.png")
plt.clf()

plt.figure()
plt.scatter(day_temp, cnt_day)
plt.plot(X_test, bayesian_pred, color="red")
plt.title("Bayesian: Day Temperature vs. Rider Count")
plt.xlabel("Temperature [deg C]")
plt.ylabel("Rider Count")
plt.savefig("images/bayesian.png")
plt.clf()