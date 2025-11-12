# Note: Requires 'folium' library (pip install folium)

import folium

# Create a folium map centered around India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add a marker for a few world countries
folium.Marker([37.7749, -122.4194], popup='USA').add_to(m)
folium.Marker([35.8617, 104.1954], popup='China').add_to(m)
folium.Marker([20.5937, 78.9629], popup='India').add_to(m)

# Add a marker for a few Indian states
folium.Marker([19.7515, 75.7139], popup='Maharashtra').add_to(m)
folium.Marker([27.0238, 74.2179], popup='Rajasthan').add_to(m)

# Save the map
m.save("world_and_india_visualization_simple.html")
print("Map saved to world_and_india_visualization_simple.html")
