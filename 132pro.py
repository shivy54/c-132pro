import pandas as pd
import matplotlib.pyplot as plt

# Import the data from the csv file
data = pd.read_csv("cleaned.csv")

# Create lists of mass, radius, and gravity data
mass_data = data["mass"].tolist()
radius_data = data["radius"].tolist()
gravity_data = data["gravity"].tolist()

# Sort the list using the sort() method
mass_data.sort()
radius_data.sort()
gravity_data.sort()

# Using Matplotlib, create charts between mass and radius
plt.scatter(mass_data, radius_data)
plt.xlabel("Mass (kg)")
plt.ylabel("Radius (m)")
plt.title("Mass vs Radius")
plt.show()

# Create a chart of mass and gravity
plt.scatter(mass_data, gravity_data)
plt.xlabel("Mass (kg)")
plt.ylabel("Gravity (m/s^2)")
plt.title("Mass vs Gravity")
plt.show()
