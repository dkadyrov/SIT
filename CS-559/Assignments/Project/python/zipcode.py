#%%
import pandas as pd
from uszipcode import SearchEngine

search = SearchEngine(simple_zipcode=True)

header = ["Zipcode", "Positive", "Total Tested", "Percentage"]
nyc_cor = pd.read_csv('..//data//nyc-coronavirus-data//tests-by-zcta.csv', skiprows=[0,1], names=header)
nyc_cor["Zipcode"] = nyc_cor["Zipcode"].astype(str)
nyc_cor.head()

zipcode_db = pd.DataFrame(columns=["Zipcode", "Population", "Population Density", "Housing Units", "Occupied Housing Units", "Median Home Value","Median Household Income"])

for index, zipcode in nyc_cor.iterrows():
    data = search.by_zipcode(zipcode["Zipcode"]).to_dict()
    zipcode_db = zipcode_db.append({
        "Zipcode": data["zipcode"],
        "Population": data["population"], 
        "Population Density": data["population_density"], 
        "Housing Units": data["housing_units"],
        "Occupied Housing Units": data["occupied_housing_units"],
        "Median Home Value": data["median_home_value"],
        "Median Household Income": data["median_household_income"], 
    }, ignore_index=True)

zipcode_db.to_csv('../data/export/zipcode_data.csv', index=False)  


# %%
