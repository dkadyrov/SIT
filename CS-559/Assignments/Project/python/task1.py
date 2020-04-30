# %%
import plotly.io as pio
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score as scorer
from scipy.optimize import curve_fit
# %%
import pandas as pd

df = pd.read_csv('../data/novel-corona-virus-2019-dataset/covid_19_data.csv',
                 parse_dates=['Last Update'])
df.rename(columns={'ObservationDate': 'Date',
                   'Country/Region': 'Country'}, inplace=True)

df["Country"].replace(["Mainland China"], ["China"], inplace=True)
df["Country"].replace(["US"], ["United States"], inplace=True)
df["Country"].replace(["UK"], ["United Kingdom"], inplace=True)

df = df.drop(columns="SNo")

df["Eradicated"] = df["Deaths"] + df["Recovered"]
df["Active"] = df["Confirmed"] - df["Eradicated"]

# %%
import pycountry_convert as pc

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

with open('../report/tables/task1_world.tex', 'w') as tf:
    tf.write(
        continents.to_latex(index=False))

def f0(x):
    return "%s"%x

def f1(x):
    return '%i'%x

# %%
fig = go.Figure()

date = df.groupby("Date")["Confirmed"].sum().reset_index()["Date"].values

for c in continents["Continent"]:
    fig.add_trace(
        go.Scatter(
            x=df[df['Continent'] == c].groupby(
                "Date")["Confirmed"].sum().reset_index()["Date"],
            y=df[df['Continent'] == c].groupby("Date")["Confirmed"].sum().reset_index()[
                "Confirmed"].values,
            name=c,
        )
    )

fig.update_layout(
    yaxis_title="Number of Confirmed Cases",
    font={
        "family": "Courier New, monospace",
    },
    legend={
        "x": 0,
        "y": 1
    },
)
fig.write_image("../images/continent.png")

# %%
def polynomial_model(data):
    x = data.loc[(data['Date'] < "04/01/2020")]["Days"].values.reshape(-1, 1)
    y = data.loc[(data['Date'] < "04/01/2020")
                 ]["Confirmed"].values.reshape(-1, 1)

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

    x2_poly = poly_features.fit_transform(x2)
    y2_pred = poly_reg.predict(x2).flatten()

    days = poly_features.fit_transform(data["Days"].values.reshape(-1, 1))
    data["Polynomial"] = poly_reg.predict(
        data["Days"].values.reshape(-1, 1)).flatten()

    score = scorer(y2, y2_pred)

    return data, score, min_deg

def exponential_model(data):
    def exponential(x, a, b, c):
        return a*np.exp(b*(x-c))

    x = data.loc[(data['Date'] < "04/01/2020")]["Days"].values
    y = data.loc[(data['Date'] < "04/01/2020")]["Confirmed"].values

    x2 = data.loc[(data['Date'] >= "04/01/2020")]["Days"]
    y2 = data.loc[(data['Date'] >= "04/01/2020")]["Confirmed"].values
    params, corr = curve_fit(exponential, x, y, p0=[0, 0, 0])

    y_test_pred = exponential(x2, *params)

    data["Exponential"] = exponential(
        data['Days'].values, *params)
    score = scorer(y2, y_test_pred)

    return data, score

def quadratic_model(data):
    def quadratic(x, a, b, c):
        return a*(x**2.0) + b*x + c

    x = data.loc[(data['Date'] < "04/01/2020")]["Days"].values
    y = data.loc[(data['Date'] < "04/01/2020")]["Confirmed"].values

    x2 = data.loc[(data['Date'] >= "04/01/2020")]["Days"]
    y2 = data.loc[(data['Date'] >= "04/01/2020")]["Confirmed"].values
    params, corr = curve_fit(quadratic, x, y, p0=[1, 1, 1])

    y_test_pred = quadratic(x2, *params)

    data["Quadratic"] = quadratic(
        data['Days'].values, *params)
    score = scorer(y2, y_test_pred)

    return data, score

def logistic_model(data):
    def logistic(x, L, k, x0):
        return L/(1+np.exp(-k*(x-x0)))

    scale = data["Confirmed"].values[-1]

    x = data.loc[(data['Date'] < "04/01/2020")]["Days"].values
    y = data.loc[(data['Date'] < "04/01/2020")]["Confirmed"].values / scale

    x2 = data.loc[(data['Date'] >= "04/01/2020")]["Days"]
    y2 = data.loc[(data['Date'] >= "04/01/2020")]["Confirmed"].values

    # x = country["Days"].values

    params, cov = curve_fit(logistic, x, y, maxfev=10000000)

    y_test_pred = logistic(x2, *params)*scale

    data["Logistic"] = logistic(data['Days'].values, *params)*scale

    score = scorer(y2, y_test_pred)

    threshold = 1.000001
    L, k, x0 = params
    last_day = int(
        round((-1/k)*np.log((1-threshold)/(threshold*np.exp(-k)-1))+x0))

    return data, score, last_day

def graph(data, name):
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=data['Date'],
            y=data["Confirmed"],
            name="Confirmed",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Exponential'],
            name="Exponential",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Quadratic'],
            name="Quadratic",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Logistic'],
            name="Logistic",
        )
    )

    fig.update_layout(
        title_x=0.5,
        yaxis={
            "range": [0, max(data["Confirmed"])+.25*max(data["Confirmed"])]
        },
        yaxis_title="Number of Confirmed Cases",
        yaxis_rangemode = "nonnegative",
        font={
            "family": "Courier New, monospace",
        },
        legend={
            "x": 0,
            "y": 1
        },
        shapes=[
            dict(
                type="rect",
                xref="x",
                yref="paper",
                x0="04/01/2020",
                y0=0,
                x1=max(data["Date"]),
                y1=1,
                fillcolor="LightSalmon",
                opacity=0.5,
                layer="below",
                line_width=0,
            )
        ],
    )
    fig.write_image("../images/task1/{}.png".format(name), scale=2)

# %%
country_data = pd.DataFrame(
    columns=["Country", "Exponential", "Quadratic", "Logistic"])
for co in continents["Continent"]:
    for c in df[df["Continent"] == co].groupby("Country").sum().sort_values(
            by=['Confirmed'], ascending=False).reset_index().head(3)["Country"]:
        print(c)
        country = df[df['Country'] == c].groupby(
            "Date")[["Date", "Confirmed"]].sum().reset_index()
        country["Days"] = country.index
        country, score1 = exponential_model(country)
        country, score2 = quadratic_model(country)
        country, score4, last_day = logistic_model(country)
        graph(country, c)
        country_data = country_data.append({
            "Country": c,
            "Exponential": score1,
            "Quadratic": score2,
            "Logistic": score4
        }, ignore_index=True)
    with open('../report/tables/{}.tex'.format(co), 'w') as tf:
        tf.write(df[df["Continent"] == co].groupby("Country").sum().sort_values(
            by=['Confirmed'], ascending=False).reset_index().head().to_latex(index=False))

with open('../report/tables/task1_country_results.tex', 'w') as tf:
    tf.write(
        country_data.sort_values("Country").to_latex(index=False))

# %%
continent_data = pd.DataFrame(
    columns=["Continent", "Exponential", "Quadratic", "Logistic"])
for co in continents["Continent"]:
    continent = df[df['Continent'] == co].groupby(
        "Date")[["Date", "Confirmed"]].sum().reset_index()

    continent["Days"] = continent.index
    continent, score1 = exponential_model(continent)
    continent, score2 = quadratic_model(continent)
    continent, score4, last_day = logistic_model(continent)
    graph(continent, co)
    continent_data = continent_data.append({
        "Continent": co,
        "Exponential": score1,
        "Quadratic": score2,
        "Logistic": score4
    }, ignore_index=True)

with open('../report/tables/task1_continent_results.tex', 'w') as tf:
    tf.write(
        continent_data.sort_values("Continent").to_latex(index=False))

# %%
world_data = pd.DataFrame(columns=["Exponential", "Quadratic", "Polynomial"])
world = df.groupby("Date")[["Date", "Confirmed"]].sum().reset_index()
world["Days"] = world.index
world, score1 = exponential_model(world)
world, score2 = quadratic_model(world)
world, score4, last_day = logistic_model(world)
graph(world, "the World")
world_data = world_data.append({
    "Exponential": score1,
    "Quadratic": score2,
    "Logistic": score4
}, ignore_index=True)

with open('../report/tables/task1_world_results.tex', 'w') as tf:
    tf.write(
        world_data.to_latex(index=False))
