import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def load_data(file_path="realdata.csv"):
  df = pd.read_csv(file_path)
  stars = df.to_dict(orient="records")
  return stars



def plot_stars(stars):
    x_coords = [star["X"] for star in stars]
    y_coords = [star["Y (light-years)"] for star in stars]
    plt.figure(figsize=(8, 8))
    plt.scatter(x_coords, y_coords, s=20)  # Adjust point size (s) as needed
    plt.xlabel("X (light-years)")
    plt.ylabel("Y (light-years)")
    plt.title("Star Positions on Cartesian Plane")
    for star in stars:
        plt.annotate(star["IAU Name"], (star["X (light-years)"], star["Y (light-years)"]), textcoords="offset points", xytext=(5,5), ha='left')
    plt.grid(True)
    plt.show()








def build_graph(stars, max_dist=100):
    graph = {}
    for star1 in stars:
        graph[star1['IAU Name']] = []
        for star2 in stars:
            if star1["IAU Name"] != star2["IAU Name"]:
                dist = np.sqrt((star1["X (light-years)"]-star2["X (light-years)"])**2 + (star1["Y (light-years)"] - star2["Y (light-years)"])**2)
                if dist < max_dist:
                    graph[star1['IAU Name']].append(star2['IAU Name'])
    return graph






def dfs(graph, start_node, visited_nodes=None):
    if visited_nodes is None:
      visited_nodes = []
    visited_nodes.append(start_node)
    for next_node in graph[start_node]:
        if next_node not in visited_nodes:
          dfs(graph, next_node, visited_nodes)
    return visited_nodes

def bfs(graph, start_node):
  visited_nodes = [start_node]
  queue = [start_node]
  while queue:
    current_node = queue.pop(0)
    for next_node in graph[current_node]:
      if next_node not in visited_nodes:
        visited_nodes.append(next_node)
        queue.append(next_node)
  return visited_nodes

def visualize_traversal(stars, graph, visited_nodes):
    plot_stars(stars)
    plt.figure(figsize=(8, 8))
    x_coords = [star["X (light-years)"] for star in stars]
    y_coords = [star["Y (light-years)"] for star in stars]
    
    for star in stars:
      if star['IAU Name'] in visited_nodes:
         plt.scatter(star["X (light-years)"], star["Y (light-years)"], s=20, color="red")  # Adjust point size (s) as needed
      else:
        plt.scatter(star["X (light-years)"], star["Y (light-years)"], s=20, color="blue")  # Adjust point size (s) as needed
    
    for node_id, neighbors in graph.items():
        star_node = next(star for star in stars if star["IAU Name"] == node_id)
        for neighbor_id in neighbors:
            star_neighbor = next(star for star in stars if star["IAU Name"] == neighbor_id)
            if neighbor_id in visited_nodes:
              plt.plot([star_node["X (light-years)"], star_neighbor["X (light-years)"]], [star_node["Y (light-years)"], star_neighbor["Y (light-years)"]], color="



            