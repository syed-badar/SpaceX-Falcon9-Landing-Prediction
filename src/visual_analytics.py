import folium
import pandas as pd
from folium.plugins import MarkerCluster

def create_map():
    site_map = folium.Map(location=[28.57, -80.64], zoom_start=5)
    marker_cluster = MarkerCluster().add_to(site_map)
    # Add dummy marker for example
    folium.Marker([28.5623, -80.5774], popup='CCAFS LC-40').add_to(marker_cluster)
    site_map.save('outputs/launch_site_map.html')
    print("Map saved to outputs/launch_site_map.html")

if __name__ == "__main__":
    create_map()