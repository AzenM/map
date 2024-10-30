import requests
import folium
from folium.plugins import MarkerCluster

BASE_URL = "https://apidata-338754564953.europe-west9.run.app"
COLORS = [
    "red", "blue", "green", "purple", "orange", "darkred", "lightred", "beige",
    "darkblue", "darkgreen", "cadetblue", "pink", "lightblue"
]

DATA_ENDPOINTS = {
    "csnj": ("/api/implantation/csnj", "red"),
    "cirfa": ("/api/implantation/cirfa", "blue"),
    "smv": ("/api/implantation/smv", "green"),
    "epide": ("/api/implantation/epide", "purple"),
    "e2c": ("/api/implantation/e2c", "orange"),
    "bases_defense": ("/api/implantation/bases_defense", "darkred"),
    "cfa": ("/api/education/cfa", "lightred"),
    "lycees": ("/api/education/lycees", "beige"),
    "enseignement_superieur": ("/api/education/enseignement_superieur", "darkblue"),
    "structures_retour_ecole": ("/api/education/structures_retour_ecole", "darkgreen"),
    "stationnements": ("/infrastructures/stationnements", "pink"),
    "gares": ("/infrastructures/gares", "lightblue")
}

def combined_map():
    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    for key, (endpoint, color) in DATA_ENDPOINTS.items():
        try:
            response = requests.get(f"{BASE_URL}{endpoint}")
            response.raise_for_status()  # Check for request errors
            data = response.json()

            for elt in data:
                try:
                    latitude, longitude = None, None
                    if key == "csnj":
                        coord_gps = elt.get("coordonnees_gps", "").replace("N", "").replace("E", "").replace("S", "").replace("W", "").replace("/", "").replace(",", ".")
                        latitude, longitude = map(float, coord_gps.split())
                    elif key == "enseignement_superieur":
                        geo = elt.get("Géolocalisation", "").strip()
                        if geo:
                            latitude, longitude = map(float, geo.replace(" ", "").replace(",", " ").split())
                        else:
                            print(f"No geolocation available for: {elt}")
                            continue
                    else:
                        latitude = float(elt.get("Latitude") or elt.get("latitude") or elt.get("Ylat") or elt.get("y_lat") or elt.get("Y_WGS84"))
                        longitude = float(elt.get("Longitude") or elt.get("longitude") or elt.get("Xlong") or elt.get("x_long") or elt.get("X_WGS84"))

                    if latitude is not None and longitude is not None:
                        folium.Marker(
                            location=[latitude, longitude],
                            popup=f"{elt}",
                            icon=folium.Icon(color=color)
                        ).add_to(marker_cluster)
                except (ValueError, TypeError) as e:
                    print(f"Error processing element {elt}: {e}")
        except requests.RequestException as e:
            print(f"Error fetching data from endpoint {endpoint}: {e}")

    my_map.save("all.html")

if __name__ == "__main__":
    combined_map()
