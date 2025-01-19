import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#works
def load_data(file_path="realdata.csv"):
  df = pd.read_csv(file_path)
  stars = df.to_dict(orient="records")
  return stars

#convert to a dictonary since no need to clean data

def plot_stars(stars):
    x_coords = [star["X"] for star in stars]
    y_coords = [star["Y"] for star in stars]
    plt.figure(figsize=(8, 8))
    plt.scatter(x_coords, y_coords, s=20)  # Adjust point size (s) as needed
    plt.xlabel("X (light-years)")
    plt.ylabel("Y (light-years)")
    plt.title("Star Positions on Cartesian Plane")
    for star in stars:
        plt.annotate(star["IAU Name"], (star["X"], star["Y"]), textcoords="offset points", xytext=(5,5), ha='left')
    plt.grid(True)
    plt.show(block=True)
