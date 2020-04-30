import numpy as np
import pandas as pd
import plotly.graph_objects as go
import pycountry_convert as pc
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error
from scipy.optimize import curve_fit
from lmfit import Model


def exponential_model(data):
    def exponential(x, a, b, c):
        return a*np.exp(b*(x-c))

    x = data.loc[(data['Date'] < "04/01/2020")]["Days"].values
    y = data.loc[(data['Date'] < "04/01/2020")]["Confirmed"].values

    x2 = data.loc[(data['Date'] >= "04/01/2020")]["Days"]
    y2 = data.loc[(data['Date'] >= "04/01/2020")]["Confirmed"].values
    exp_fit = curve_fit(exponential, x, y, p0=[0, 0, 0])

    y_test_pred = exponential(x2, *exp_fit[0])

    data["Exponential"] = exponential(
        data['Days'].values, *exp_fit[0])
    score = r2_score(y2, y_test_pred)

    return data, score

# def sinusoidal(data):
#     # def guassian(x, a, x0, sigma):
#     #     return a*np.exp(-(x-x0)**2/(2*sigma**2))
#     # def guassian(x, mean, std):
#     #     return 1/(std*np.sqrt(2*np.pi))*np.exp(-((x-mean)**2)/(2*std**2))

#     def wave(x, amp, freq):
#         return amp*np.sin(x*freq)

#     x = data.loc[(data['Date'] < "04/01/2020")]["Days"].values
#     y = data.loc[(data['Date'] < "04/01/2020")]["Confirmed"].values

#     x2 = data.loc[(data['Date'] >= "04/01/2020")]["Days"]
#     y2 = data.loc[(data['Date'] >= "04/01/2020")]["Confirmed"].values

#     # mean = 
#         # sigma = sum(y * (x - mean)**2)

#     g_fit = curve_fit(gaussian, x, y, p0=[1,0,1])

#     y_test_pred = gaussian(x2, *g_fit[0])

#     data["Gaussian"] = gaussian(
#         data['Days'].values, *g_fit[0])
#     score = r2_score(y2, y_test_pred)

#     return data, score

def quadratic_model(data):
    def quadratic(E,a,b,c):    
        B = (a*(E**2.0)) + (b*E) + c
        return B

    x = data.loc[(data['Date'] < "04/01/2020")]["Days"].values
    y = data.loc[(data['Date'] < "04/01/2020")]["Confirmed"].values

    x2 = data.loc[(data['Date'] >= "04/01/2020")]["Days"]
    y2 = data.loc[(data['Date'] >= "04/01/2020")]["Confirmed"].values
    exp_fit = curve_fit(quadratic, x, y, p0=[1, 1, 1])

    y_test_pred = quadratic(x2, *exp_fit[0])

    data["Quadratic"] = quadratic(
        data['Days'].values, *exp_fit[0])
    score = r2_score(y2, y_test_pred)

    return data, score    
# def polynomial(x_train, x_test, y_train, y_test, deg):
#     poly_reg = PolynomialFeatures(degree=deg)
#     x_poly = poly_reg.fit_transform(x_train)

#     lr = LinearRegression()
#     lr.fit(x_poly, y_train)

#     x_poly_test = poly_reg.fit_transform(x_test)
#     y_pred = lr.predict(x_poly_test)
#     poly_mse = mean_squared_error(y_test, y_pred)
#     poly_rmse = np.sqrt(poly_mse)

#     return lr, poly_mse, poly_rmse

# def optimize_lr(x_train, x_test, y_train, y_test):
#     rmses = []
#     degrees = np.arange(1, 10)
#     min_rmse, min_deg = 1e10, 0

#     for deg in degrees:
#         lr, poly_mse, poly_rmse = polynomial(
#             x_train, x_test, y_train, y_test, deg)

#         # Cross-validation of degree
#         if min_rmse > poly_rmse:
#             min_rmse = poly_rmse
#             min_deg = deg

#     return lr, min_deg, min_rmse

# def polynomial_model(country):

    # x = country.loc[(country['Date'] < "04/01/2020")]["Days"].values
    # y = country.loc[(country['Date'] < "04/01/2020")]["Confirmed"].values

    # x2 = country.loc[(country['Date'] >= "04/01/2020")
    #                  ]["Days"].values.reshape(-1, 1)
    # y2 = country.loc[(country['Date'] >= "04/01/2020")
    #                  ]["Confirmed"].values.reshape(-1, 1)

    # x_train, x_test, y_train, y_test = train_test_split(
    #     x.reshape(-1, 1), y.reshape(-1, 1), test_size=0.30, random_state=42)

    # lr, min_deg, min_rmse = optimize_lr(x_train, x_test, y_train, y_test)

    # poly_reg = PolynomialFeatures(degree=min_deg)
    # # x_poly = poly_reg.fit_transform(x.reshape(-1, 1))

    # # lr = LinearRegression()
    # # lr.fit(x_poly, y.reshape(-1,1))

    # # To retrieve the intercept:
    # # print(lr.intercept_)
    # # For retrieving the slope:
    # # print(lr.coef_)
    # # print(type(lr))
    # # print(x2)

    # x_poly_test = poly_reg.fit_transform(x_test)
    # # y_pred = lr.predict(x_poly_test)    

    # y_test_pred = lr.predict(x_poly_test)
    # country["Polynomial"] = lr.predict(poly_reg.fit_transform(
    #     country["Days"].values.reshape(-1, 1))).flatten()

    # # y_pred_future = lr.predict(poly_reg.fit_transform(check["Days"].values.reshape(-1,1))).flatten()

    # # lr.score(y_pred)
    # score = r2_score(y2, y_test_pred)

    # return country, score

def get_continent(row):
    continents = {
        'NA': 'North America',
        'SA': 'South America',
        'AS': 'Asia',
        'OC': 'Australia',
        'AF': 'Africa',
        'EU': 'European Union'
    }

    country = row["Country"]
    try:
        country_code = pc.country_name_to_country_alpha2(
            country, cn_name_format="default")
        return continents[pc.country_alpha2_to_continent_code(country_code)]
    except:
        return None



df = pd.read_csv('./data/novel-corona-virus-2019-dataset/covid_19_data.csv',
                 parse_dates=['Last Update'])
df.rename(columns={'ObservationDate': 'Date',
                   'Country/Region': 'Country'}, inplace=True)
df.drop(columns="SNo")
df["Eradicated"] = df["Deaths"] + df["Recovered"]
df["Active"] = df["Confirmed"] - df["Eradicated"]

df["Country"].replace(["Mainland China"], ["China"], inplace=True)
df["Country"].replace(["US"], ["United States"], inplace=True)
df["Country"].replace(["UK"], ["United Kingdom"], inplace=True)

# df = df.groupby('Date').sum()['Deaths'].reset_index()
# df["Days"] = df.index

past = df.loc[(df['Date'] == "04/01/2020")]
future = df.loc[(df['Date'] > "04/01/2020")]


df["Continent"] = df.apply(lambda row: get_continent(row), axis=1)

# NA = ['US', 'Canada', 'Mexico']
# Asia = ['Iran', 'South Korea', 'Japan']
# Africa = ["Morocco", "Egypt", "Algeria"]
# Europe = ["Spain", "Italy", "Germany"]
# SA = ["Brazil", "Peru", "Ecuador"]
continents = df.groupby("Continent").sum().sort_values(
    by=['Confirmed'], ascending=False).reset_index()

print(continents.to_latex(index=False))

# df[df["Continent"] == "Australia"].groupby("Country").sum().sort_values(
#     by=['Confirmed'], ascending=False).reset_index().head()





name = "South Korea"

country = df[df['Country'] == name].groupby(
    "Date")[["Date", "Confirmed"]].sum().reset_index()
country["Days"] = country.index
country = country.loc[(country['Confirmed'] > 0.01*country['Confirmed'].max())]

def polynomial_model(data): 
    x = data.loc[(data['Date'] < "04/01/2020")]["Days"].values.reshape(-1, 1)
    y = data.loc[(data['Date'] < "04/01/2020")]["Confirmed"].values.reshape(-1, 1)

    x2 = data.loc[(data['Date'] >= "04/01/2020")
                        ]["Days"].values.reshape(-1, 1)
    y2 = data.loc[(data['Date'] >= "04/01/2020")
                        ]["Confirmed"].values.reshape(-1, 1)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.30, random_state=42)

    rmses = []
    degrees = np.arange(1, 10)
    min_rmse, min_deg = 1e10, 0

    for deg in degrees:
        # Train features
        poly_features = PolynomialFeatures(degree=deg, include_bias=False)
        x_poly_train = poly_features.fit_transform(x_train)

        # Linear regression
        poly_reg = LinearRegression()
        poly_reg.fit(x_poly_train, y_train)

        # Compare with test data
        x_poly_test = poly_features.fit_transform(x_test)
        poly_predict = poly_reg.predict(x_poly_test)
        poly_mse = mean_squared_error(y_test, poly_predict)
        poly_rmse = np.sqrt(poly_mse)
        rmses.append(poly_rmse)

        # Cross-validation of degree
        if min_rmse > poly_rmse:
            min_rmse = poly_rmse
            min_deg = deg

    poly_features = PolynomialFeatures(degree=min_deg, include_bias=False)
    x_poly = poly_features.fit_transform(x)

    poly_reg = LinearRegression()
    poly_reg.fit(x, y)


    days = poly_features.fit_transform(data["Days"].values.reshape(-1,1))

    data["Polynomial"] = poly_reg.predict(data["Days"].values.reshape(-1,1)).flatten()
    score = 0 

    return data, score

country, score1 = polynomial_model(country)
country, score2 = exponential_model(country)
country, score4 = quadratic_model(country)
graph(country, name)
