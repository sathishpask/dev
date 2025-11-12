# Note: Requires 'folium' library (pip install folium)

import folium
from folium import GeoJson # Required import

# Load a GeoJSON dataset (countries boundary data)
geojson_data = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"

# Create a folium map centered at [0, 0]
m = folium.Map(location=[0, 0], zoom_start=2)

# Add GeoJSON data to the map with interaction features
GeoJson(
    geojson_data,
    name='geojson',
    style_function=lambda x: {'fillColor': 'green', 'color': 'black'},
    highlight_function=lambda x: {'fillColor': 'yellow', 'color': 'blue'},
    tooltip=folium.features.GeoJsonTooltip(fields=['name'], labels=False, sticky=False)
).add_to(m)

# Add layer control for user interaction
folium.LayerControl().add_to(m)

# Save the map as an HTML file
m.save("interactive_map_with_interaction.html")
print("Map saved to interactive_map_with_interaction.html")
