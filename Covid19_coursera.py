# This Code will use John Hopkins Dataset and also happiness dataset

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

corona_dataset = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
corona_dataset.head(10)
corona_dataset.shape()

df = corona_dataset.drop(["Lat", "Long"], axis=1)
#   df = corona_dataset.drop(["Lat", "Long"], axis=1, inplace = True) # if you want to replace in corona_dataset
df.head(10)

corona_dataset_aggregated = corona_dataset.groupby("Country/Region").sum()
corona_dataset_aggregated.head(10)
corona_dataset_aggregated.shape()

corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Italy"].plot()
corona_dataset_aggregated.loc["Spain"].plot()
plt.legend()

corona_dataset_aggregated.loc["China"][:10].plot()
corona_dataset_aggregated.loc["Italy"].diff().plot()
corona_dataset_aggregated.loc["Italy"].diff().max()

# witch country has the most infected
countries = list(corona_dataset_aggregated.index)
max_infection_rate = []
for c in countries:
    max_infection_rate.append(corona_dataset_aggregated.loc[c].diff().max())
max_infection_rate

# add max infection rate column
corona_dataset_aggregated["max_infection_rate"] = max_infection_rate
corona_dataset_aggregated.head()

# delet other data from data set
corona_data_max_infected = pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])

happiness_report = pd.read_csv("Datasets/worldwide_happiness_report.csv")
happiness_report.head(10)
useless_col = ["Overall rank", "Score", "Generosity", "Perceptions of corruption"]
happiness_report.drop(useless_col, axis=1, inplace=True)
happiness_report.head(10)

happiness_report.set_index("Country or region", inplace=True)
happiness_report.head()
happiness_report.shape()
corona_data_max_infected.shape()

new_data = corona_data_max_infected.join(happiness_report, how="inner")
new_data.head()

# Measure the Correlation
new_data.corr()

#   Visualize
new_data.head()

x = new_data["GDP per capita"]
y = new_data["max_infection_rate"]
sns.scatterplot(x, np.log(y))

sns.regplot(x, np.log(y))
