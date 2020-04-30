# %% 
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import pycountry_convert as pc
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error
from scipy.optimize import curve_fit
from datetime import datetime, timedelta
from math import trunc 

# %% 
df = pd.read_csv('../data/novel-corona-virus-2019-dataset/covid_19_data.csv', parse_dates=['Last Update'])
df.rename(columns={'ObservationDate': 'Date',
                   'Country/Region': 'Country'}, inplace=True)

df = df.drop(columns="SNo")

df["Eradicated"] = df["Deaths"] + df["Recovered"]
df["Active"] = df["Confirmed"] - df["Eradicated"]

df["Country"].replace(["Mainland China"], ["China"], inplace=True)
df["Country"].replace(["US"], ["United States"], inplace=True)
df["Country"].replace(["UK"], ["United Kingdom"], inplace=True)

import pycountry_convert as pc

def f0(x):
    return "%s"%x

def f1(x):
    return '%i'%x

def get_continent(row):
    continents = {
        'NA': 'North America',
        'SA': 'South America',
        'AS': 'Asia',
        'OC': 'Oceania',
        'AF': 'Africa',
        'EU': 'Europe'
    }

    country = row["Country"]
    try:
        country_code = pc.country_name_to_country_alpha2(
            country, cn_name_format="default")
        return continents[pc.country_alpha2_to_continent_code(country_code)]
    except:
        return None

df["Continent"] = df.apply(lambda row: get_continent(row), axis=1)
continents = df.groupby("Continent").sum().sort_values(
    by=['Confirmed'], ascending=False).reset_index()

# %%

def logistic(x, L, k, x0): 
    return L/(1+np.exp(-k*(x-x0)))

def logistic_model(x_train, y_train, x_pred):

    scale = y_train[-1]
    y_train = y_train / scale

    params, cov = curve_fit(logistic, x_train, y_train, maxfev=10000000)

    y_pred = logistic(x_pred, *params) * scale

    return y_pred, params

def predict_day(params): 
    threshold = 1.000001
    L, k, x0 = params
    last_day = int(round((-1/k)*np.log((1-threshold)/(threshold*np.exp(-k)-1))+x0))

    return last_day

def predict(x, y): 
    days = np.arange(0, len(x))#np.linspace(0, len(x)-1, len(x))

    y_pred, params = logistic_model(days, y, days)

    last_day = predict_day(params)

    if last_day > days[-1]:
        future_days = np.linspace(0, last_day, last_day+1)
    else: 
        future_days = np.linspace(0, days[-1], days[-1]+1)
    # print(future_days)

    future, params = logistic_model(days, y, future_days)
    d0 = datetime.strptime(x[0], '%m/%d/%Y')
    future_dates = [datetime.strftime(d0+timedelta(days=d), '%m/%d/%Y') for d in future_days]

    return future_dates, future
# %%
def graph(data, name, confirmed, deaths=None, recovered=None, filename=None, show=None):
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            # x = data["Date"],
            x=[confirmed[0][x] for x in data["Date"].index],    
            y=data["Confirmed"],
            name="Confirmed",
            marker_color='#1f77b4'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=confirmed[0],     
            y=confirmed[1],
            name="Confirmed Model",
            marker_color='#1f77b4',
            showlegend=False
        )
    )

    if deaths: 
        fig.add_trace(
            go.Bar(
                x=[deaths[0][x] for x in data["Date"].index],     
                y=data["Deaths"],
                name="Deaths",
                marker_color='#ff7f0e'
            )
        )

        fig.add_trace(
            go.Scatter(
                x=deaths[0],     
                y=deaths[1],
                name="Deaths Model",
                marker_color='#ff7f0e',
                showlegend=False
            )
        )

    if recovered:
        fig.add_trace(
            go.Bar(
                x=[recovered[0][x] for x in data["Date"].index],     
                y=data["Recovered"],
                name="Recovered",
                marker_color='#2ca02c'
            )
        )

        fig.add_trace(
            go.Scatter(
                x=recovered[0],     
                y=recovered[1],
                name="Recovered Model",
                marker_color='#2ca02c',
                showlegend=False
            )
        )

    fig.update_layout(
        title_x = 0.5,
        yaxis_title="Number of Cases",
        font={
            "family":"Courier New, monospace",
        },
        legend={
            "x": 0,
            "y": 1
        },
    )


    if show: 
        fig.show()

    else: 
        if filename: 
            fig.write_image("../images/task2/{}.png".format(filename), scale=2)
        else: 
            fig.write_image("../images/task2/{}.png".format(name), scale=2)

 # %%
continent_data = pd.DataFrame(columns=["Continent", "End Date", "Total Confirmed", "Total Deaths"])
country_data = pd.DataFrame(columns=["Country", "End Date", "Total Confirmed", "Total Deaths"])

for co in df.groupby("Continent").sum().sort_values(
    by=['Confirmed'], ascending=False).reset_index()["Continent"]:
    
    data = df[df['Continent'] == co].groupby(
            "Date")[["Date", "Confirmed", "Recovered", "Deaths"]].sum().reset_index()

    confirmed = predict(data["Date"].values, data["Confirmed"].values)
    recovered = predict(data["Date"].values, data["Recovered"].values)
    deaths = predict(data["Date"].values, data["Deaths"].values)

    graph(data, co, confirmed, deaths, recovered)
    graph(data, co, confirmed, deaths, filename="{}_c_d".format(co))
    graph(data, co, confirmed, filename="{}_c".format(co))

    continent_data = continent_data.append({
        "Continent": co, 
        "End Date": confirmed[0][-1], 
        "Total Confirmed": confirmed[1][-1], 
        "Total Deaths": deaths[1][-1]
    }, ignore_index=True)

    for c in df[df["Continent"] == co].groupby("Country").sum().sort_values(
        by=['Confirmed'], ascending=False).reset_index().head(3)["Country"]:
        
        data = df[df['Country'] == c].groupby(
            "Date")[["Date", "Confirmed", "Recovered", "Deaths"]].sum().reset_index()

        try: 
            confirmed = predict(data["Date"].values, data["Confirmed"].values)
            recovered = predict(data["Date"].values, data["Recovered"].values)
            deaths = predict(data["Date"].values, data["Deaths"].values)

            graph(data, c, confirmed, deaths, recovered)
            graph(data, c, confirmed, deaths, filename="{}_c_d".format(c))
            graph(data, c, confirmed, filename="{}_c".format(c))

            country_data = country_data.append({
                "Country": c, 
                "End Date": confirmed[0][-1], 
                "Total Confirmed": confirmed[1][-1], 
                "Total Deaths": deaths[1][-1]
            }, ignore_index=True)
        except: 
            print(c)


with open('../report/tables/task2_continent_results.tex', 'w') as tf:
    tf.write(
        continent_data.sort_values("Continent").to_latex(index=False, formatters=[f0, f0, f1, f1]))

with open('../report/tables/task2_country_results.tex', 'w') as tf:
    tf.write(
        country_data.sort_values("Country").to_latex(index=False, formatters=[f0, f0, f1, f1]))

# %% 
world_data = pd.DataFrame(columns= ["End Date", "Total Confirmed", "Total Deaths"])
data = df.groupby("Date")[["Date", "Confirmed", "Recovered", "Deaths"]].sum().reset_index()
confirmed = predict(data["Date"].values, data["Confirmed"].values)
recovered = predict(data["Date"].values, data["Recovered"].values)
deaths = predict(data["Date"].values, data["Deaths"].values)

graph(data, "the World", confirmed, deaths)
world_data = world_data.append({
    "End Date": confirmed[0][-1], 
    "Total Confirmed": confirmed[1][-1], 
    "Total Deaths": deaths[1][-1]
}, ignore_index=True)

with open('../report/tables/task2_world_results.tex', 'w') as tf:
    tf.write(
        world_data.to_latex(index=False, formatters=[f0, f1, f1]))

