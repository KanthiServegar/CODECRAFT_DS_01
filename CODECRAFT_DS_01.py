import pandas as pd
import matplotlib.pyplot as plt
# Load main population CSV file (skip first 4 rows as they are headers or notes)
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_5830.csv", skiprows=4)

# Show first few rows
print(df.head())
# Select Country and 2022 population only
df_2022 = df[["Country Name", "2022"]].dropna()

# Sort by population (descending) and select top 10
top10 = df_2022.sort_values(by="2022", ascending=False).head(10)
print(top10)
# Plot Bar Chart
plt.figure(figsize=(10,6))
plt.bar(top10["Country Name"], top10["2022"], color="skyblue")
plt.xticks(rotation=45)
plt.title("Top 10 Most Populated Countries (2022)")
plt.xlabel("Country")
plt.ylabel("Population")
plt.tight_layout()
plt.show()

# Plot Histogram
plt.figure(figsize=(10,6))
plt.hist(df_2022["2022"], bins=30, color="purple")
plt.title("Population Distribution Across Countries (2022)")
plt.xlabel("Population")
plt.ylabel("Number of Countries")
plt.show()
