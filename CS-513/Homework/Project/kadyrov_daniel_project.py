# Course: CS 513B
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Project

# %% 
import pandas as pd 

data = pd.read_csv("attrition_data.csv",  keep_default_na=False)

# %%
features = pd.DataFrame()

# Annual Rate
features["annual rate"] = data["ANNUAL_RATE"]
# features["annual rate"] = pd.cut(data["ANNUAL_RATE"],  [0, 20000, 50000, 75000, 100000, 2000000], labels=[1,2,3,4,5])

# Hourly Rate
features["hourly rate"] = data["HRLY_RATE"]
# features["hourly rate"] = pd.cut(data["HRLY_RATE"],  [0, 25, 50, 75, 100, 1000], labels=[1,2,3,4,5])

#Factorize Ethnicities
ethnicities = pd.factorize(data["ETHNICITY"])
features["ethnicity"] = ethnicities[0]

#Facotirze Sex
sex = pd.factorize(data["SEX"])
features["sex"] = sex[0]

#Marital Status
marital = pd.factorize(data["MARITAL_STATUS"])
features["marital"] = marital[0]

# Job Satisfaction
features["satisfaction"] = data["JOB_SATISFACTION"]

# Age
# features["age"] = pd.cut(data["AGE"], [0, 20, 30, 50, 60, 100], labels=[1,2,3,4,5])
features["age"] = data["AGE"]

# Number of Teams
team_num = pd.factorize(data["NUMBER_OF_TEAM_CHANGED"])
features["number of teams"] = team_num[0]


# Hire Month
hire_month = pd.factorize(data["HIRE_MONTH"])
# features["hire month"] = hire_month[0]
features["hire month"] = pd.cut(hire_month[0], [0, 2, 5, 6, 11], labels=[1,2,3,4], include_lowest=True)

# First Job
first_job = pd.factorize(data["IS_FIRST_JOB"])
features["first job"] = first_job[0]

# Travel 
travel = pd.factorize(data["TRAVELLED_REQUIRED"])
features["travel"] = travel[0]

# Performance
features["rating"] = data["PERFORMANCE_RATING"]

# Disabled
disabled = pd.factorize(data["DISABLED_EMP"])
features["disabled emp"] = disabled[0]

vet = pd.factorize(data["DISABLED_VET"])
features["disabled vet"] = vet[0]

education = pd.factorize(data["EDUCATION_LEVEL"])
features["education"] = education[0]

# status = pd.DataFrame({
# classification["actual"] = data["STATUS"]
status = pd.factorize(data["STATUS"])
classification = pd.DataFrame(data=status[0], columns=["status"])
# classification["actual norm "] = status[0]

group = pd.factorize(data["JOB_GROUP"])
features["group"] = group[0]
#%%
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(features, classification, test_size=0.3, random_state=7)

# classification = pd.DataFrame()
# classification["actual"] = y_train
# classification["actual"].append(y_test, ignore_index=True)
#%% 
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2)
kmeans.fit(x_train)

# classification["kmeans"]
# %%
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, 
                               bootstrap = True,
                               max_features = 'sqrt')

#%%
import matplotlib.pyplot as plt

plt.scatter(x_train["annual rate"], x_train["age"], label=kmeans.labels_, c=kmeans.labels_)
plt.show()

# %%
import plotly.express as px
# df = px.data.iris()
fig = px.scatter_matrix(x_train, color=kmeans.labels_)
fig.update_traces(diagonal_visible=False, showupperhalf=False)
fig.show()

# %%
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=x_train["hourly rate"],
        y=x_train["age"],
        mode="markers",
        marker= {
            "color":kmeans.labels_
        },
        # name = kmeans.labels_
        text=kmeans.labels_,
    )
)
fig.update_layout(
    xaxis_title="Hourly Rate",
    yaxis_title="Age",
)
fig.show()

# fig.write_image("../images/task5/task5_timeline.png")

# %%
import plotly.express as px
df = px.data.tips()
df["size"] = df["size"].astype(str)
fig = px.scatter(x=x_train["hourly rate"],
        y=x_train["age"], color=kmeans.labels_,
                 title="String 'size' values mean discrete colors")

fig.show()

# %%
