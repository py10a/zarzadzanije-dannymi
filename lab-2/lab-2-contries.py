import folium
import json
import pandas as pd

world_json_location = "/Users/py10/projects/zarzadzanije-dannymi/lab-2/world.json"

world_map = folium.Map(
    location=[20, 0],
    zoom_start=2,
    tiles='OpenStreetMap'
)

with open(world_json_location, 'r', encoding='utf-8') as file:
    world_data = json.load(file)

countries_data = []
for feature in world_data['features']:
    properties = feature['properties']
    countries_data.append({
        'ISO3': properties.get('ISO3', ''),
        'NAME': properties.get('NAME', ''),
        'POP2005': properties.get('POP2005', 0),
        'REGION': properties.get('REGION', ''),
        'SUBREGION': properties.get('SUBREGION', '')
    })

df = pd.DataFrame(countries_data)

df_filtered = df[df['POP2005'] > 0].copy()


folium.Choropleth(
    geo_data=world_data,
    name="Населення країн",
    data=df_filtered,
    columns=['ISO3', 'POP2005'],
    key_on='feature.properties.ISO3',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Населення (2005)',
    bins=8,
    nan_fill_color='lightgray'
).add_to(world_map)

folium.GeoJson(
    world_data,
    name="Інформація про країни",
    tooltip=folium.GeoJsonTooltip(
        fields=['NAME', 'POP2005', 'REGION'],
        aliases=['Країна:', 'Населення (2005):', 'Регіон:'],
        localize=True,
        sticky=False,
        labels=True,
        style="""
            background-color: yellow;
            border: 2px solid black;
            border-radius: 3px;
            box-shadow: 3px;
        """
    )
).add_to(world_map)

folium.LayerControl().add_to(world_map)

world_map.save("./lab-2/index.html")
