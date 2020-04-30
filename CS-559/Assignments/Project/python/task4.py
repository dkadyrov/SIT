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
                   'Country/Region': 'Country',
                   'Province/State': 'State'
                   }, inplace=True)

df = df.drop(columns="SNo")

df["Eradicated"] = df["Deaths"] + df["Recovered"]
df["Active"] = df["Confirmed"] - df["Eradicated"]

df["Country"].replace(["Mainland China"], ["China"], inplace=True)
df["Country"].replace(["US"], ["United States"], inplace=True)
df["Country"].replace(["UK"], ["United Kingdom"], inplace=True)

# %%

state = df[df["Country"] =="United States"].groupby("State").sum().sort_values(  
    by=['Confirmed'], ascending=False).reset_index().head(10)

with open('../report/tables/task4_states.tex', 'w') as tf:
    tf.write(state.to_latex(index=False))

# %%
weather_data = pd.read_csv("../data/weather/weather.csv", parse_dates=["DATE"]) 
weather_data["DATE"] = weather_data["DATE"].dt.strftime('%m/%d/%Y')
# %%
ny_weather = weather_data[weather_data["STATION"] == "USW00094789"]
la_weather = weather_data[weather_data["STATION"] == "USW00023174"]
no_weather = weather_data[weather_data["STATION"] == "USW00012916"]
dt_weather = weather_data[weather_data["STATION"] == "USW00014822"]

#%% 
def graphs(data, name): 
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x = data["DATE"],
            y = data["TMAX"], #/ np.linalg.norm(data["Growth Rate"])
            line_color='#1f77b4'
        )
    )
    fig.add_trace(
        go.Scatter(
            x = data["DATE"],
            y = data["TMIN"], #/ np.linalg.norm(data["Growth Rate"])
            fill='tonexty',
            line_color='#1f77b4'
        )
    )

    fig.update_layout(
        title_x = 0.5,
        yaxis_title="Temperature (deg F)",

        font={
            "family":"Courier New, monospace",
        },
        legend={
            "x": 0,
            "y": 1
        },
        showlegend=False
    )
    fig.write_image("../images/task4/{}_temp.png".format(name), scale=2)

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x = data["DATE"],
            y = data["PRCP"], #/ np.linalg.norm(data["Growth Rate"])
        )
    )

    fig.update_layout(
        title_x = 0.5,
        yaxis_title="Precipitation (in)",

        font={
            "family":"Courier New, monospace",
        },
        legend={
            "x": 0,
            "y": 1
        },
        showlegend=False
    )
    fig.write_image("../images/task4/{}_rain.png".format(name), scale=2)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x = data["DATE"],
            y = data["AWND"], #/ np.linalg.norm(data["Growth Rate"])
        )
    )

    fig.update_layout(
        title_x = 0.5,
        yaxis_title="Average Wind Speed (mph)",

        font={
            "family":"Courier New, monospace",
        },
        legend={
            "x": 0,
            "y": 1
        },
        showlegend=False
    )
    fig.write_image("../images/task4/{}_wnd.png".format(name), scale=2)

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x = data["Date"],
            y = data["Confirmed"], #/ np.linalg.norm(data["Growth Rate"])
            name = "Confirmed"
        )
    )

    fig.add_trace(
        go.Bar(
            x = data["Date"],
            y = data["Deaths"], #/ np.linalg.norm(data["Growth Rate"])
            name = "Deaths"
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
    fig.write_image("../images/task4/{}_cases.png".format(name), scale=2)    
# %%
ny = pd.merge(left=df[df['State'] == "New York"].groupby(
            "Date")[["Date", "Confirmed", "Deaths"]].sum().reset_index(), right=ny_weather[["DATE", "AWND", "PRCP", "TMAX", "TMIN"]], left_on="Date", right_on="DATE") 
ny.corr().style.background_gradient('viridis')
graphs(ny, "New York")

with open('../report/tables/task4_newyork.tex', 'w') as tf:
    tf.write(ny.corr().to_latex())

# %%
la = pd.merge(left=df[df['State'] == "California"].groupby(
            "Date")[["Date", "Confirmed", "Deaths"]].sum().reset_index(), right=la_weather[["DATE", "AWND", "PRCP", "TMAX", "TMIN"]], left_on="Date", right_on="DATE") 
la.corr().style.background_gradient('viridis')
graphs(la, "California")

with open('../report/tables/task4_california.tex', 'w') as tf:
    tf.write(la.corr().to_latex())

# %%
dt = pd.merge(left=df[df['State'] == "Michigan"].groupby(
            "Date")[["Date", "Confirmed", "Deaths"]].sum().reset_index(), right=la_weather[["DATE", "AWND", "PRCP", "TMAX", "TMIN"]], left_on="Date", right_on="DATE") 
dt.corr().style.background_gradient('viridis') 
graphs(dt, "Michigan")

with open('../report/tables/task4_michigan.tex', 'w') as tf:
    tf.write(dt.corr().to_latex())

# %% 

no = pd.merge(left=df[df['State'] == "Louisiana"].groupby(
            "Date")[["Date", "Confirmed", "Deaths"]].sum().reset_index(), right=la_weather[["DATE", "AWND", "PRCP", "TMAX", "TMIN"]], left_on="Date", right_on="DATE") 
no.corr().style.background_gradient('viridis') 
graphs(no, "Loisiana")

with open('../report/tables/task4_louisiana.tex', 'w') as tf:
    tf.write(no.corr().to_latex())


# %%
