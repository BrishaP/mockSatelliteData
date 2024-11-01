import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import folium  # JUST IN CASE for future mapping

# Define Locations with Latitude and Longitude
# Using dictionary to store location names and coordinates
locations = {
    "Location1": (52.5200, 13.4050),   # Berlin
    "Location2": (48.8566, 2.3522),    # Paris
    "Location3": (40.7128, -74.0060),  # New York
    "Location4": (34.0522, -118.2437), # Los Angeles
    "Location5": (35.6895, 139.6917)   # Tokyo
}

# Generate Dates for 1-Year Period
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(365)]  # 1 year of data

# Create Synthetic Data for Each Location
data = []
for location, (lat, lon) in locations.items():
    for date in dates:
        temp = np.random.normal(15, 10)  # Mean temperature 15°C, std deviation 10
        veg_index = np.random.uniform(0, 1)  # Vegetation index between 0 and 1
        data.append([location, lat, lon, date, temp, veg_index])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Location", "Latitude", "Longitude", "Date", "Temperature", "Vegetation_Index"])

# Print the first few rows to check the data
print(df.head())

# visualization using Folium

#Initialize the map
# Center the map based on the average latitude and longitude of all locations
m = folium.Map(location=[df["Latitude"].mean(), df["Longitude"].mean()], zoom_start=2)

# Add data points to the map
# Loop through each row in DataFrame
for _, row in df.iterrows():
    # Define a color based on temperature
    color = "blue" if row["Temperature"] < 15 else "red"  # Example color based on temperature

    # Add a circle marker for each location
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=5,  # Radius of the circle
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=(
            f"Location: {row['Location']}<br>"
            f"Date: {row['Date'].strftime('%Y-%m-%d')}<br>"
            f"Temperature: {row['Temperature']:.2f}°C<br>"
            f"Vegetation Index: {row['Vegetation_Index']:.2f}"
        )
    ).add_to(m)

# Save the map as HTML file
m.save("map.html")
print("Map has been saved as map.html")