# %%
#documentation for folium: https://python-visualization.github.io/folium/latest/index.html
import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium

# %%
idaho_places = pd.read_parquet("./data/idaho_places.parquet")

st.title("DEMO: Folium")


# %%
lds_churches = idaho_places[idaho_places['location_name'] == "The Church of Jesus Christ of Latter day Saints"] 

# %%
#example code
# map = folium.Map(location=[bike_station_locations.Latitude.mean(), bike_station_locations.Longitude.mean()], zoom_start=14, control_scale=True
# for index, location_info in bike_station_locations.iterrows():
#    folium.Marker([location_info["Latitude"], location_info["Longitude"]], popup=location_info["Name"]).add_to(map)

# %%
# render = st_folium(map)
# to render chart in instance, comment the above code and uncomment the below
#map
# %%

#type streamlit run folium_demo.py in terminal to render streamlit application