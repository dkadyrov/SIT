#%%
import pandas as pd
from uszipcode import SearchEngine


# search = SearchEngine(simple_zipcode=True)

# subway_db = pd.read_csv("..//data//nyc//Stations.csv")

# subway = pd.DataFrame(columns=["ID", "Name", "Division", "Borough", "Zipcode", "Lines", "Latitude", "Longitude"])
# # test = search.by_coordinates(40.785672, -73.95107, radius=1, returns=1)
# for index, station in subway_db.iterrows():
#     try:  
#         zipcode = search.by_coordinates(station["GTFS Latitude"], station["GTFS Longitude"], radius=2, returns=1)[0].to_dict()["zipcode"]
#         subway = subway.append({
#             "ID": station["Station ID"],
#             "Name": station["Stop Name"],
#             "Division": station["Division"],
#             "Borough": station["Borough"],
#             "Zipcode": zipcode, 
#             "Lines": station["Daytime Routes"],
#             "Latitude": station["GTFS Latitude"], 
#             "Longitude": station["GTFS Longitude"]
#         }, ignore_index=True)
#     except:
#         print(station["Station ID"])
# subway.to_csv('../data/export/stations.csv', index=False)  
# # zipcode = search.by_zipcode("10016")

# %%
import csv

stations = pd.read_csv("..//data//export//stations.csv")
zipcode = {}#pd.DataFrame(columns=["Zipcode", "Lines"])
 
for index, station in stations.iterrows(): 
    if station["Zipcode"] in zipcode.keys(): 
        for line in station["Lines"].split(" "): 
            if line not in zipcode[station["Zipcode"]]:
                zipcode[station["Zipcode"]].append(line)

    else: 
        zipcode[station["Zipcode"]] = station["Lines"].split(" ")

# zip_sub = pd.DataFrame.from_dict(zipcode)
# zip_sub.to_csv('../data/export/zipcode_subway.csv', index=False)  
name = '../data/export/zipcode_subway.csv'
with open(name, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Zipcode", "Lines"])
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)

# %%
