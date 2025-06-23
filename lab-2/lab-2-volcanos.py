import folium, pandas

world_json_location = "/Users/py10/projects/zarzadzanije-dannymi/lab-2/world.json"
volcanoes_txt_location = "/Users/py10/projects/zarzadzanije-dannymi/lab-2/Volcanoes.txt"

df = pandas.read_csv(volcanoes_txt_location) 
world_map = folium.Map(0, 0)

group_volcanos = folium.FeatureGroup("Volcanos").add_to(world_map) 
for index, row in df.iterrows():
    folium.Marker(
        location=(row['LAT'], row['LON']), 
        popup=f"Name: {row['NAME']}\nElevation: {row['ELEV']}",
        icon=folium.Icon("red")
    ).add_to(group_volcanos)

folium.LayerControl().add_to(world_map) 

world_map.save("./lab-2/index.html")
