#generates an interactive map using folium which shows a world map, with an overlay of volcanoes
#and population density

import folium
import pandas as pd

data = pd.read_csv("Volcanoes_USA.txt")

LAT = list(data["LAT"])
LON = list(data["LON"])
ELEV = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.23, -98.58], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(LAT,LON,ELEV):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+"m", 
    fill_color=color_producer(el), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green'if x['properties']['POP2005'] <10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")