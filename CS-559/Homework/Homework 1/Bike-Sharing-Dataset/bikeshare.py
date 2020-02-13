import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso, BayesianRidge
from sklearn.model_selection import KFold
from sklearn import metrics
import numpy as np

hour = pd.read_csv("hour.csv")
day = pd.read_csv("day.csv")

cnt_hour = hour["cnt"].values.reshape(-1, 1)
cnt_day = day["cnt"].values.reshape(-1, 1)
day_temp = day["temp"].values.reshape(-1, 1) * 41

def make_graphs():
    plt.figure()
    plt.scatter(hour["registered"].values.reshape(-1, 1),
                cnt_hour, label="registered")
    plt.scatter(hour["casual"].values.reshape(-1, 1), cnt_hour, label="casual")
    plt.title("Hourly Users")
    plt.legend()
    plt.savefig("images/hour_users")
    plt.clf()

    for col in range(len(hour.columns)):
        if hour.columns[col] not in ["instant", "cnt", "dteday", "registered", "casual"]:
            plt.figure()
            plt.scatter(hour[hour.columns[col]].values.reshape(-1, 1), cnt_hour)
            plt.title("{} vs. Total Rider Hourly Count".format(hour.columns[col]))
            plt.xlabel("{}".format(hour.columns[col]))
            plt.ylabel("{}".format("Total Rider Count"))
            plt.savefig("images/hour_{}.png".format(hour.columns[col]))
            plt.clf()


    plt.figure()
    plt.scatter(hour["registered"].values.reshape(-1, 1), cnt_hour)
    plt.scatter(hour["casual"].values.reshape(-1, 1), cnt_hour)
    plt.savefig("images/day_users")
    plt.clf()

    for col in range(len(day.columns)):
        if day.columns[col] not in ["instant", "cnt", "dteday", "registered", "casual"]:
            plt.figure()
            plt.scatter(day[day.columns[col]].values.reshape(-1, 1), cnt_day)
            plt.title("{} vs. Total Rider Daily Count".format(day.columns[col]))
            plt.xlabel("{}".format(day.columns[col]))
            plt.ylabel("{}".format("Total Rider Count"))
            plt.legend()
            plt.savefig("images/day_{}.png".format(day.columns[col]))
            plt.clf()

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
    # bayesian.fit(X_train, y_train)
    

linear_pred = linear.predict(X_test)
ridge_pred = ridge.predict(X_test)
lasso_pred = lasso.predict(X_test)
# bayesian_pred = bayesian.predict(X_test)

mse_linear = metrics.mean_squared_error(y_test, linear_pred)
mse_ridge = metrics.mean_squared_error(y_test, ridge_pred)
mse_lasso = metrics.mean_squared_error(y_test, lasso_pred)
# mse_bayesian = metrics.mean_squared_error(y_test, bayesian_pred)

plt.figure()
plt.scatter(day_temp, cnt_day)
plt.plot(X_test, linear_pred, color="red", label=mse_linear)
plt.plot(X_test, ridge_pred, color="purple", label=mse_ridge)
plt.plot(X_test, lasso_pred, color="orange", label=mse_lasso)
# plt.plot(X_test, bayesian_pred, color="green", label=mse_bayesian)

plt.title("Day Temperature vs. Rider Count")
plt.xlabel("Temperature [deg C]")
plt.ylabel("Rider Count")
plt.legend()
plt.show()