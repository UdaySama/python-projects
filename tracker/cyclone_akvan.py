#pip install folium

import folium

ucoding = folium.Map(
    location=[17.7, 84.9],
    zoom_start=6,
    tiles="OpenStreetMap"
)

folium.Marker(
    location=[17.7, 84.9],
    tooltip="Cyclone Akvan",
    popup="IMD position: 20 Nov,02:30 IST",
    icon=folium.Icon(color='blue',icon="cloud")
).add_to(ucoding)

ucoding.save("cyclone_map.html")

