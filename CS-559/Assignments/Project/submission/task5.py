# %% 
import pandas as pd
import numpy as np

header = ["Zipcode", "Positive", "Total Tested", "Percentage"]
nyc_cor = pd.read_csv('../data//nyc-coronavirus-data//tests-by-zcta.csv', skiprows=[0,1], names=header)
nyc_cor["Zipcode"] = nyc_cor["Zipcode"].astype(str)

# %%
table = nyc_cor[["Zipcode", "Positive"]].sort_values(  
    by=['Positive'], ascending=False).reset_index().head(10)

with open('../report/tables/task5_zips.tex', 'w') as tf:
    tf.write(table.to_latex(index=False))
#%%
stations = pd.read_csv("..//data//export//stations.csv")
subway_lines = {}#pd.DataFrame(columns=["Zipcode", "Lines"])
 
for index, station in stations.iterrows(): 
    if station["Zipcode"] in subway_lines.keys(): 
        for line in station["Lines"].split(" "): 
            if line not in subway_lines[station["Zipcode"]]:
                subway_lines[station["Zipcode"]].append(line)

    else: 
        subway_lines[station["Zipcode"]] = station["Lines"].split(" ")
# %%
nyc_dem = pd.read_csv("../data//nyc//Demographic_Statistics_By_Zip_Code.csv")
nyc_dem["JURISDICTION NAME"] = nyc_dem["JURISDICTION NAME"].astype(str)
# %%
nyc = pd.merge(left=nyc_cor, right=nyc_dem, left_on="Zipcode", right_on="JURISDICTION NAME")
nyc = nyc.drop(columns="JURISDICTION NAME")

# %%
nyc["Lines"] = None

for index, zipcode in nyc.iterrows(): 
    try: 
        nyc.at[index, 'Lines'] = subway_lines[int(zipcode["Zipcode"])]
    except: 
        nyc.at[index, 'Lines'] = []


nyc["Num Lines"] = nyc["Lines"].apply(
    lambda x: len(x))

# %%
zipcode_db = pd.read_csv("../data//export//zipcode_data.csv")
zipcode_db["Zipcode"] = zipcode_db["Zipcode"].astype(str)
nyc = pd.merge(left=nyc, right=zipcode_db, left_on="Zipcode", right_on="Zipcode")

#%%

nyc.sort_values(  
    by=['Positive'], ascending=False).reset_index().head(10)

correlate_positive = nyc.drop(columns=["Positive"]).corrwith(nyc["Positive"])
with open('../report/tables/task5_correlation.tex', 'w') as tf:
    tf.write(correlate_positive.to_latex())

# %% 

#%%
import folium
map = folium.Map(location=[40.693943, -73.985880], default_zoom_start=1, tiles='Mapbox Bright')


map.choropleth(geo_data="..\\data\\nyc_shape\\zipcode.geojson",
             data=nyc, # my dataset
             columns=['Zipcode', 'Positive'], # zip code is here for matching the geojson zipcode, sales price is the column that changes the color of zipcode areas
             key_on='feature.properties.postalCode', # this path contains zipcodes in str type, this zipcodes should match with our ZIP CODE column
             fill_color='BuPu', fill_opacity=1, line_opacity=0.2)
map.save("map")

# %%
from datetime import datetime

headers = ["Date", "Confirmed", "Hospitalized", "Deaths"]
nyc_time = pd.read_csv('..//data//nyc-coronavirus-data//case-hosp-death.csv', skiprows=[0,1], names=headers)

nyc_time["Deaths"] = nyc_time["Deaths"].fillna(0)

nyc_time["Confirmed Sum"] = nyc_time["Confirmed"].cumsum()
nyc_time["Hospitalized Sum"] = nyc_time["Hospitalized"].cumsum()
nyc_time["Deaths Sum"] = nyc_time["Deaths"].cumsum()

nyc_time["Date"] = nyc_time["Date"].apply(
    lambda x: datetime.strftime(
        datetime.strptime(x, "%m/%d/%y"), "%m/%d/%Y"))


#%%
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=nyc_time["Date"],
        y=nyc_time["Confirmed Sum"],
        name="Confirmed"
    )
)

fig.add_trace(
    go.Bar(
        x=nyc_time["Date"],
        y=nyc_time["Hospitalized Sum"],
        name="Hospitalized"
    )
)

fig.add_trace(
    go.Bar(
        x=nyc_time["Date"],
        y=nyc_time["Deaths Sum"],
        name="Deaths"
    )
)

fig.update_layout(
    title_x=0.5,

    yaxis_title="Number of Cases",
    font={
        "family": "Courier New, monospace",
    },
    legend={
        "x": 0,
        "y": 1
    },
)
fig.write_image("../images/task5/task5_timeline.png")
# %%
from task2 import logistic_model, predict_day
from datetime import datetime, timedelta

def predict(data):
    def predict_day(params): 
        threshold = 1.000001
        L, k, x0 = params
        last_day = int(round((-1/k)*np.log((1-threshold)/(threshold*np.exp(-k)-1))+x0))

        return last_day

    def predict(x, y): 
        days = np.arange(0, len(x))

        y_pred, params = logistic_model(days, y, days)

        last_day = predict_day(params)

        if last_day > days[-1]:
            future_days = np.linspace(0, last_day, last_day+1)
        else: 
            future_days = np.linspace(0, days[-1], days[-1]+1)

        future, params = logistic_model(days, y, future_days)
        d0 = datetime.strptime(x[0], '%m/%d/%Y')
        future_dates = [datetime.strftime(d0+timedelta(days=d), '%m/%d/%Y') for d in future_days]

        return future_dates, future

    days = np.arange(0, len(nyc_time["Date"]))#np.linspace(0, len(x)-1, len(x))
    cmodel, params = logistic_model(days, data.values, days)
    last_day = predict_day(params)
    if last_day > len(nyc_time["Date"]):
        future_days = np.linspace(0, last_day, last_day+1)

    future, params = logistic_model(days, data.values, future_days)
    d0 = datetime.strptime(nyc_time["Date"].values[0], '%m/%d/%Y')
    future_dates = [datetime.strftime(d0+timedelta(days=d), '%m/%d/%Y') for d in future_days]

    return future_dates, future

confirmed = predict(nyc_time["Confirmed Sum"])
hospitalized = predict(nyc_time["Hospitalized Sum"])
deaths = predict(nyc_time["Deaths Sum"])

#%%
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Bar(
        # x = data["Date"],
        x=nyc_time["Date"],    
        y=nyc_time["Confirmed Sum"],
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
            x=nyc_time["Date"],    
            y=nyc_time["Deaths Sum"],
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

if hospitalized:
    fig.add_trace(
        go.Bar(
            x=nyc_time["Date"],    
            y=nyc_time["Deaths Sum"],
            name="Hospitalized",
            marker_color='#2ca02c'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=hospitalized[0],     
            y=hospitalized[1],
            name="Hospitalized Model",
            marker_color='#2ca02c',
            showlegend=False
        )
    )


fig.update_layout(
    title_x=0.5,

    yaxis_title="Number of Cases",
    font={
        "family": "Courier New, monospace",
    },
    legend={
        "x": 0,
        "y": 1
    },
)

fig.write_image("../images/task5/modeling.png")

# %%
nyc_pred = {
    "End Date": [confirmed[0][-1]],
    "Total Confirmed": [int(confirmed[1][-1])], 
    "Total Hospitalized": [int(hospitalized[1][-1])],
    "Total Deaths": [int(deaths[1][-1])]
}

results = pd.DataFrame(data = nyc_pred)

# %%
from task3 import growth_rate

nyc_time["Growth Rate"] = growth_rate(nyc_time["Confirmed Sum"])

# %%
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=nyc_time["Date"],
        y=nyc_time["Growth Rate"],
        # name="Confirmed"
    )
)

fig.update_layout(
    title_x=0.5,
    yaxis_title="Growth Rate",
    font={
        "family": "Courier New, monospace",

    },
    legend={
        "x": 0,
        "y": 1
    },
)
fig.write_image("../images/task5/task5_growthrate.png")

