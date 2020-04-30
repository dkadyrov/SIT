# %%
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
from scipy.stats import linregress

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

#%% 
def growth_rate(data=None):
    x = []
    x.append(0)
    for i in range(data.shape[0]-1):
        next
        a = abs(data.iloc[i+1]-data.iloc[i])
        if data.iloc[i] == 0:
            v = 0.0
        else:
            v = a/data.iloc[i]
        v=v*100
        x.append(v)
        
    return np.array(x)

df["Growth Rate"] = growth_rate(df["Confirmed"])

# %%
name = "Australia"

data = df[df['Country'] == name].groupby("Date")[["Date", "Confirmed", "Deaths", "Recovered", "Active", "Growth Rate"]].sum().reset_index()

y = data[data["Date"].between("03/20/2020", "03/24/2020")]["Growth Rate"]
# y = data.loc[(data["Growth Rate"] > 0.01*data["Growth Rate"].max()) & (data["Growth Rate"] < data["Growth Rate"].max()) & (data["Growth Rate"].index < data["Growth Rate"].idxmax())]["Growth Rate"]
# y = data.loc[(data["Growth Rate"] > 0.01*data["Growth Rate"].max())]["Growth Rate"]
# y = data["Growth Rate"]
# y = data.loc[(data["Confirmed"] > 0.01*data["Confirmed"].max()) & (data["Confirmed"] < data["Confirmed"].max()) & (data["Confirmed"].index < data["Confirmed"].idxmax())]["Growth Rate"]

x = y.index

regressor = LinearRegression()  
regressor.fit(x.values.reshape(-1,1), y.values.reshape(-1,1))

y2 = regressor.predict(x.values.reshape(-1,1)).flatten()

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x = data["Date"],
        y = data["Growth Rate"], #/ np.linalg.norm(data["Growth Rate"])
        name="Growth Rate"
    )
)
fig.add_trace(
    go.Scatter(
        x = data["Date"][x],
        y = y2, #/np.linalg.norm(data["Confirmed"])
        name="Model"
    )
)

fig.update_layout(
    # title="COVID19 Growth Rate in {}".format(name),
    title_x = 0.5,
    # xaxis_title="Date",
    # xaxis= {
    #     'tickformat': '%b',
    #     # 'tickvals': pd.date_range('2020-1', '2020-4', freq='MS')
    # },
    # xaxis = {
    #     # 'type':'category'
    #     'tickvals': confirmed[0],
    #     'ticktext': confirmed[0]
    # },
    yaxis_title="Growth Rate (%)",
    # yaxis = {
    #     'rangemode': "tozero",
    # },
    yaxis_rangemode = "nonnegative",
    font={
        "family":"Courier New, monospace",
        # size=18,
        # color="#7f7f7f"
    },
    legend={
        "x": 0,
        "y": 1
    },
)
fig.write_image("../images/task3/Australia.png", scale=2)


# %%
slope = regressor.coef_
startdate = data.loc[(data["Growth Rate"] > 0.01*data["Growth Rate"].max())]["Date"].values[0]
# enddate = data.loc[(data["Growth Rate"].index > data["Growth Rate"].idxmax()) & (data["Growth Rate"] < 0.01*data["Growth Rate"].max())]["Date"].values[0]


# %%
