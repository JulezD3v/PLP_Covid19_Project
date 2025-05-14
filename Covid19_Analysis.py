# # COVID-19 Global Data Analysis Project

# 🚩 Project Overview:
# This notebook analyses global COVID-19 data focusing on cases, deaths, recoveries, and vaccinations across time and countries.

# ## 📦 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px





df = pd.read_csv('PLP_Covid19_Project\owid-covid-data.csv')

#Checking if I have the right columns
print(df.columns)
print(df.head())

# Setup plotting aesthetics
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)



# ## 👀 3. Initial Exploration
print("Columns:")
print(df.columns)

print("\nPreview:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())



# Filter selected countries
countries = ["Kenya", "India", "United States"]
df = df[df["location"].isin(countries)]

# Drop rows with missing critical data
df.dropna(subset=["total_cases", "total_deaths", "total_vaccinations", "new_cases", "new_deaths"], inplace=True)

# Fill missing values for numeric columns
df.fillna(method="ffill", inplace=True)

# ## 📊 5. Exploratory Data Analysis

# Line plot: Total cases over time
plt.figure()
for country in countries:
    country_data = df[df["location"] == country]
    plt.plot(country_data["date"], country_data["total_cases"], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.show()

# Line plot: Total deaths over time
plt.figure()
for country in countries:
    country_data = df[df["location"] == country]
    plt.plot(country_data["date"], country_data["total_deaths"], label=country)
plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.show()

# Compare daily new cases
sns.lineplot(data=df, x="date", y="new_cases", hue="location")
plt.title("Daily New COVID-19 Cases")
plt.show()

# Death rate
df["death_rate"] = df["total_deaths"] / df["total_cases"]
sns.lineplot(data=df, x="date", y="death_rate", hue="location")
plt.title("COVID-19 Death Rate Over Time")
plt.ylabel("Death Rate")
plt.show()

# ## 💉 6. Vaccination Analysis

# Cumulative vaccinations
plt.figure()
for country in countries:
    country_data = df[df["location"] == country]
    plt.plot(country_data["date"], country_data["total_vaccinations"], label=country)
plt.title("Cumulative COVID-19 Vaccinations")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.show()

# Optional pie chart (static example)
latest_date = df["date"].max()
latest_data = df[df["date"] == latest_date]
latest_data = latest_data[["location", "total_vaccinations"]].set_index("location")
latest_data.plot.pie(y="total_vaccinations", autopct="%1.1f%%", legend=False)
plt.title("Vaccination Distribution (Latest Date)")
plt.ylabel("")
plt.show()

# ## 🌍 7. Choropleth Map (Optional)
map_df = pd.read_csv("owid-covid-data.csv")
map_df = map_df[map_df["date"] == map_df["date"].max()]
map_fig = px.choropleth(map_df,
                        locations="iso_code",
                        color="total_cases",
                        hover_name="location",
                        title="Total COVID-19 Cases by Country",
                        color_continuous_scale="Reds")
map_fig.show()

