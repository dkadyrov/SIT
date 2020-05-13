# Course: CS 513B
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Project

# %% 
import pandas as pd 
import numpy as np

data = pd.read_csv("attrition_data.csv",  keep_default_na=False)

# %%
features = pd.DataFrame()

# Annual Rate
# features["annual rate"] = data["ANNUAL_RATE"]
features["annual rate"] = pd.cut(data["ANNUAL_RATE"],  [0, 20000, 50000, 75000, 100000, 2000000], labels=[1,2,3,4,5])

# Hourly Rate
# features["hourly rate"] = data["HRLY_RATE"]
features["hourly rate"] = pd.cut(data["HRLY_RATE"],  [0, 25, 50, 75, 100, 1000], labels=[1,2,3,4,5])

#Factorize Ethnicities
ethnicities = pd.factorize(data["ETHNICITY"])
features["ethnicity"] = ethnicities[0]

#Facotirze Sex
sex = pd.factorize(data["SEX"])
features["sex"] = sex[0]

#Marital Status
marital = pd.factorize(data["MARITAL_STATUS"])
features["marital"] = marital[0]

# Job Satisfactionhhave 
features["satisfaction"] = data["JOB_SATISFACTION"]

# Age
features["age"] = pd.cut(data["AGE"], [0, 20, 30, 50, 60, 100], labels=[1,2,3,4,5])
# features["age"] = data["AGE"]

# Number of Teams
team_num = pd.factorize(data["NUMBER_OF_TEAM_CHANGED"])
features["number of teams"] = team_num[0]


# Hire Month
hire_month = pd.factorize(data["HIRE_MONTH"])
features["hire month"] = hire_month[0]
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
# classification = pd.DataFrame(data=status[0], columns=["status"])
# classification["actual norm "] = status[0]

# group =
with open('features.tex', 'w') as tf:
     tf.write(pd.DataFrame(np.unique(data["JOB_GROUP"])).transpose().to_latex(header=True))

data["JOB_GROUP"].replace(['Regulatory Affairs', 'Customer Care',  'Human Resources', 'Customer Relationship Mgmt', "Sourcing", "Quality Assurance", 'Plant & Facilities Maintenance'], "Support", inplace=True)

data["JOB_GROUP"].replace(['Analytical/Microbiology', 'Industrial Quality', 'R&I Development/Pre-Develpmnt', 'R&I General Management', 'Technical Packaging','Applied Research','Package Development','Production & Operations','R&I Evaluation','R&I Safety Evaluation','Advanced Research'], "Engineering", inplace=True)

data["JOB_GROUP"].replace(['Accounting', 'Accounts Payable', 'Finance', "Treasury", "Tax", "Legal", 'Supply Chain Finance',], "Finance", inplace=True)

data["JOB_GROUP"].replace(['IT Architecture and Integrtion','IT Digital','IT Security/Risk and Quality','Web','IT Business Applications','IT Governance and Management','IT Technologies and Infrstrctr', 'Transportation & Warehousing'], "Support", inplace=True)

data["JOB_GROUP"].replace(['Flows & Sub-Contracting', 'General Management', 'Intellectual Proprty & Patents', 'Logistics - Distribution', 'Manufacturing Supply Chain', 'Market Supply Logistics', 'Multi-Channel', 'Prod Planning & Inventory Ctl', 'Supply Chain Administration', 'Corporate Supply Chain', 'Demand Planning', 'Distribution/Administration', 'General Administration', 'Insurance & Risk Management', 'Logistics - Manufacturing', 'Plant Management', 'Demi-Grand', "Physical Flows"], "Management", inplace=True)

data["JOB_GROUP"].replace(['Claims Substantiation', 'Creative Service/Copy', 'Digital', 'Integrated Marketing Comm', 'Marketing - Global', 'Promotional Purchasing', 'Integrated Mktg Communications', 'Market Research', 'Marketing - Direct', 'Marketing Support/Services', 'Social Media', 'eCommerce', 'Brand Operations', 'Public Relations'], "Marketing", inplace=True)


# data["JOB_GROUP"].replace(["Accounting", "Accounts Payable", "Claims Substantiation",  ],["Finance"], inplace=True)
# data["JOB_GROUP"].replace(["Customer Care"], ["HR"])
# data["JOB_GROUP"].replace(["Market Research", "Marketing - Direct", ])
# data["JOB_GROUP"].replace(["Advanced Research", "Accounts Payable", ],["Finance"], inplace=True)
# f["Country"].replace(["US"], ["United States"], inplace=True)

group = pd.factorize(data["JOB_GROUP"])
features["group"] = group[0]

features["prevyr_1"] = data["PREVYR_1"]
features["prevyr_2"] = data["PREVYR_2"]
features["prevyr_3"] = data["PREVYR_3"]
features["prevyr_4"] = data["PREVYR_4"]
features["prevyr_5"] = data["PREVYR_5"]

# %%
with open('report/features.tex', 'w') as tf:
     tf.write(features.head().to_latex(header=True))
with open('report/data.tex', 'w') as tf:
     tf.write(data.head().to_latex(header=True))
# %%

#correlation = features.corrwith(status[0])

#with open('correlation.tex', 'w') as tf:
#     tf.write(correlation.to_latex(header=False))

# %%
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (15,20))
ax = fig.gca()

features.hist(ax = ax)

# features.hist()
plt.savefig('hist.png')

# %%
fig = plt.figure(figsize = (15,20))
ax = fig.gca()

data["STATUS"].hist(ax = ax)

# features.hist()
plt.savefig('status.png')

#%%
# Feature Selection
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import numpy as np

lr = LogisticRegression()
rfe = RFE(lr, 10)
rfe = rfe.fit(features, status[0])

selected = pd.concat([features.iloc[:,i] for i in np.where(rfe.support_==True)])

with open('report/selected.tex', 'w') as tf:
     tf.write(selected.head().to_latex(header=True, index=False))

#%% 
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(selected, status[0], test_size=0.3, random_state=7)

#%% 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

rf = RandomForestClassifier()
rf.fit(x_train, y_train)

classification = pd.DataFrame(data=y_test, columns=["status"])
classification["rf"] = rf.predict(x_test)

accuracy = pd.DataFrame({
    "rf": [accuracy_score(classification["status"], classification["rf"])]
})

# %%
from sklearn.svm import SVC

svc = SVC()
svc.fit(x_train, y_train)

classification["svc"] = svc.predict(x_test)

accuracy["svc"] = accuracy_score(classification["status"], classification["svc"])

# %%
from sklearn.metrics import confusion_matrix
import seaborn as sns

forest_cm = confusion_matrix(classification["rf"], classification["status"], [1,0])
sns.heatmap(forest_cm, annot=True, fmt='.2f',xticklabels = ["Terminated", "Active"] , yticklabels = ["Terminated", "Active"] )
plt.ylabel('True class')
plt.xlabel('Predicted class')
plt.title('Random Forest')
plt.savefig('random_forest')

svc_cm = confusion_matrix(classification["svc"], classification["status"], [1,0])
sns.heatmap(svc_cm, annot=True, fmt='.2f',xticklabels = ["Terminated", "Active"] , yticklabels = ["Terminated", "Active"] )
plt.ylabel('True class')
plt.xlabel('Predicted class')
plt.title('SVC')
plt.savefig('svc')

# %%
from sklearn.metrics import classification_report

with open('report/classification-rf.tex', 'w') as tf:
     tf.write(pd.DataFrame(classification_report(classification["status"], classification["rf"], target_names=status[1], output_dict=True)).transpose().to_latex(header=True))

with open('report/classification-svc.tex', 'w') as tf:
     tf.write(pd.DataFrame(classification_report(classification["status"], classification["svc"], target_names=status[1], output_dict=True)).transpose().to_latex(header=True))

# %%
with open('report/accuracy.tex', 'w') as tf:
     tf.write(accuracy.to_latex(index=False))

# %%

# %%
