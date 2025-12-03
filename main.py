import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("DailyDelhiClimate.csv")

print("=== HEAD ===")
print(df.head())

print("\n=== INFO ===")
print(df.info())

print("\n=== DESCRIBE ===")
print(df.describe())

df = df.dropna()

df['date'] = pd.to_datetime(df['date'])

df = df[['date', 'meantemp', 'humidity']]

df = df.set_index('date')

print(df.head())

temps = df['meantemp'].values

print("Daily Mean Temperature:", np.mean(temps))
print("Daily Min Temperature:", np.min(temps))
print("Daily Max Temperature:", np.max(temps))
print("Daily Std Temperature:", np.std(temps))

monthly_stats = df.resample('M').mean()
print("\nMonthly Stats:")
print(monthly_stats)

yearly_stats = df.resample('Y').mean()
print("\nYearly Stats:")
print(yearly_stats)

plt.figure(figsize=(10,4))
plt.plot(df.index, df['meantemp'], color='red')
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.savefig("daily_temperature.png")
plt.show()

monthly_humidity = df['humidity'].resample('M').mean()

plt.figure(figsize=(10,4))
plt.bar(monthly_humidity.index, monthly_humidity, color='blue')
plt.title("Monthly Average Humidity")
plt.xlabel("Month")
plt.ylabel("Humidity (%)")
plt.savefig("monthly_humidity.png")
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(df['meantemp'], df['humidity'], alpha=0.5)
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.savefig("scatter_temp_vs_humidity.png")
plt.show()

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(df.index, df['meantemp'], color='orange')
plt.title("Daily Temperature")

plt.subplot(1,2,2)
plt.scatter(df['meantemp'], df['humidity'], color='green')
plt.title("Humidity vs Temperature")

plt.tight_layout()
plt.savefig("combined_plots.png")
plt.show()

df['month'] = df.index.month

monthly_group = df.groupby('month').mean()
print("Monthly Grouped Data:")
print(monthly_group)

def season(month):
    if month in [12,1,2]:
        return "Winter"
    elif month in [3,4,5]:
        return "Summer"
    elif month in [6,7,8,9]:
        return "Monsoon"
    else:
        return "Post-Monsoon"

df['season'] = df['month'].apply(season)

season_group = df.groupby('season').mean()
print("\nSeason-wise Statistics:")
print(season_group)

df.to_csv("cleaned_delhi_climate.csv")