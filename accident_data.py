import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("traffic_accident_data.csv")

plt.figure(figsize=(10, 6))
sns.countplot(x="accident_severity", data=df, palette="coolwarm")
plt.title("Accident Severity Distribution")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x="road_condition", hue="accident_severity", data=df)
plt.title("Accidents by Road Condition and Severity")
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df["longitude"], df["latitude"], alpha=0.5, c='red', s=10)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Accident Hotspots")
plt.show()

severity_counts = df.groupby(["road_condition", "weather", "time_of_day"]).size().reset_index(name='count')
print(severity_counts.sort_values(by='count', ascending=False).head(10))