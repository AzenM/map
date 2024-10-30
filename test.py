import requests
import folium
from folium.plugins import MarkerCluster

BASE_URL = "https://apidata-338754564953.europe-west9.run.app"
COLORS = [
    "red", "blue", "green", "purple", "orange", "darkred", "lightred", "beige",
    "darkblue", "darkgreen", "cadetblue", "pink", "lightblue"
]

def generate_map_csnj():
    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    try:
        response = requests.get(f"{BASE_URL}/api/implantation/csnj")
        data = response.json()

        for elt in data:
            try:
                coord_gps = elt["coordonnees_gps"].replace("N", "").replace("E", "").replace("S", "").replace("W", "").replace("/", "").replace(",", ".")
                latitude, longitude = map(float, coord_gps.split())
                folium.Marker(
                    location=[latitude, longitude],
                    popup=f"{elt}",
                    icon=folium.Icon(color="red")
                ).add_to(marker_cluster)
            except Exception as e:
                print(f"Error processing element {elt}: {e}")
    except requests.RequestException as e:
        print(f"Error fetching data from endpoint /api/implantation/csnj: {e}")

    my_map.save("csnj_map.html")

def generate_map_cirfa():
    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    try:
        response = requests.get(f"{BASE_URL}/api/implantation/cirfa")
        data = response.json()

        for elt in data:
            try:
                latitude, longitude = float(elt["latitude"]), float(elt["longitude"])
                folium.Marker(
                    location=[latitude, longitude],
                    popup=f"{elt}",
                    icon=folium.Icon(color="blue")
                ).add_to(marker_cluster)
            except Exception as e:
                print(f"Error processing element {elt}: {e}")
    except requests.RequestException as e:
        print(f"Error fetching data from endpoint /api/implantation/cirfa: {e}")

    my_map.save("cirfa_map.html")

def generate_map_smv():
    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    try:
        response = requests.get(f"{BASE_URL}/api/implantation/smv")
        data = response.json()

        for elt in data:
            try:
                latitude, longitude = float(elt["Latitude"]), float(elt["Longitude"])
                folium.Marker(
                    location=[latitude, longitude],
                    popup=f"{elt}",
                    icon=folium.Icon(color="green")
                ).add_to(marker_cluster)
            except Exception as e:
                print(f"Error processing element {elt}: {e}")
    except requests.RequestException as e:
        print(f"Error fetching data from endpoint /api/implantation/smv: {e}")

    my_map.save("smv_map.html")

def generate_map_epide():
    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    try:
        response = requests.get(f"{BASE_URL}/api/implantation/epide")
        data = response.json()

        for elt in data:
            try:
                latitude, longitude = float(elt["Latitude"]), float(elt["Longitude"])
                folium.Marker(
                    location=[latitude, longitude],
                    popup=f"{elt}",
                    icon=folium.Icon(color="purple")
                ).add_to(marker_cluster)
            except Exception as e:
                print(f"Error processing element {elt}: {e}")
    except requests.RequestException as e:
        print(f"Error fetching data from endpoint /api/implantation/epide: {e}")

    my_map.save("epide_map.html")

def generate_map_e2c():
    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    try:
        response = requests.get(f"{BASE_URL}/api/implantation/e2c")
        data = response.json()

        for elt in data:
            try:
                latitude, longitude = float(elt["Latitude"]), float(elt["Longitude"])
                folium.Marker(
                    location=[latitude, longitude],
                    popup=f"{elt}",
                    icon=folium.Icon(color="orange")
                ).add_to(marker_cluster)
            except Exception as e:
                print(f"Error processing element {elt}: {e}")
    except requests.RequestException as e:
        print(f"Error fetching data from endpoint /api/implantation/e2c: {e}")

    my_map.save("e2c_map.html")

def generate_map_bases_defense():
    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    try:
        response = requests.get(f"{BASE_URL}/api/implantation/bases_defense")
        data = response.json()

        for elt in data:
            try:
                latitude, longitude = float(elt["Latitude"]), float(elt["Longitude"])
                folium.Marker(
                    location=[latitude, longitude],
                    popup=f"{elt}",
                    icon=folium.Icon(color="darkred")
                ).add_to(marker_cluster)
            except Exception as e:
                print(f"Error processing element {elt}: {e}")
    except requests.RequestException as e:
        print(f"Error fetching data from endpoint /api/implantation/bases_defense: {e}")

    my_map.save("bases_defense_map.html")

def generate_map_cfa():
    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    try:
        response = requests.get(f"{BASE_URL}/api/education/cfa")
        data = response.json()

        for elt in data:
            try:
                latitude, longitude = float(elt["Latitude"]), float(elt["Longitude"])
                folium.Marker(
                    location=[latitude, longitude],
                    popup=f"{elt}",
                    icon=folium.Icon(color="lightred")
                ).add_to(marker_cluster)
            except Exception as e:
                print(f"Error processing element {elt}: {e}")
    except requests.RequestException as e:
        print(f"Error fetching data from endpoint /api/education/cfa: {e}")

    my_map.save("cfa_map.html")

def generate_map_lycees():
    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    try:
        response = requests.get(f"{BASE_URL}/api/education/lycees")
        data = response.json()

        for elt in data:
            try:
                latitude, longitude = float(elt["Latitude"]), float(elt["Longitude"])
                folium.Marker(
                    location=[latitude, longitude],
                    popup=f"{elt}",
                    icon=folium.Icon(color="beige")
                ).add_to(marker_cluster)
            except Exception as e:
                print(f"Error processing element {elt}: {e}")
    except requests.RequestException as e:
        print(f"Error fetching data from endpoint /api/education/lycees: {e}")

    my_map.save("lycees_map.html")

def generate_map_enseignement_superieur():
    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    try:
        response = requests.get(f"{BASE_URL}/api/education/enseignement_superieur")
        data = response.json()

        for elt in data:
            geo = elt.get("Géolocalisation", "").strip()
            if geo:
                try:
                    latitude, longitude = map(float, geo.replace(" ", "").replace(",", " ").split())
                    folium.Marker(
                        location=[latitude, longitude],
                        popup=f"{elt}",
                        icon=folium.Icon(color="darkblue")
                    ).add_to(marker_cluster)
                except Exception as e:
                    print(f"Error processing element {elt}: {e}")
            else:
                print(f"No geolocation available for: {elt}")
    except requests.RequestException as e:
        print(f"Error fetching data from endpoint /api/education/enseignement_superieur: {e}")

    my_map.save("enseignement_superieur_map.html")

def generate_map_structures_retour_ecole():
    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    try:
        response = requests.get(f"{BASE_URL}/api/education/structures_retour_ecole")
        data = response.json()

        for elt in data:
            try:
                latitude, longitude = float(elt["Latitude"]), float(elt["Longitude"])
                folium.Marker(
                    location=[latitude, longitude],
                    popup=f"{elt}",
                    icon=folium.Icon(color="darkgreen")
                ).add_to(marker_cluster)
            except Exception as e:
                print(f"Error processing element {elt}: {e}")
    except requests.RequestException as e:
        print(f"Error fetching data from endpoint /api/education/structures_retour_ecole: {e}")

    my_map.save("structures_retour_ecole_map.html")

def generate_map_stationnements():
    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    try:
        response = requests.get(f"{BASE_URL}/infrastructures/stationnements")
        data = response.json()

        for elt in data:
            try:
                latitude, longitude = float(elt["Ylat"]), float(elt["Xlong"])
                folium.Marker(
                    location=[latitude, longitude],
                    popup=f"{elt}",
                    icon=folium.Icon(color="pink")
                ).add_to(marker_cluster)
            except Exception as e:
                print(f"Error processing element {elt}: {e}")
    except requests.RequestException as e:
        print(f"Error fetching data from endpoint /infrastructures/stationnements: {e}")

    my_map.save("stationnements_map.html")

def generate_map_gares():
    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    try:
        response = requests.get(f"{BASE_URL}/infrastructures/gares")
        data = response.json()

        for elt in data:
            try:
                latitude, longitude = float(elt["Y_WGS84"]), float(elt["X_WGS84"])
                folium.Marker(
                    location=[latitude, longitude],
                    popup=f"{elt}",
                    icon=folium.Icon(color="lightblue")
                ).add_to(marker_cluster)
            except Exception as e:
                print(f"Error processing element {elt}: {e}")
    except requests.RequestException as e:
        print(f"Error fetching data from endpoint /infrastructures/gares: {e}")

    my_map.save("gares_map.html")

if __name__ == "__main__":
    generate_map_csnj()
    generate_map_cirfa()
    generate_map_smv()
    generate_map_epide()
    generate_map_e2c()
    generate_map_bases_defense()
    generate_map_cfa()
    generate_map_lycees()
    generate_map_enseignement_superieur()
    generate_map_structures_retour_ecole()
    generate_map_stationnements()
    generate_map_gares()

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

async def combined_map():
    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    for key, (endpoint, color) in DATA_ENDPOINTS.items():
        try:
            response = requests.get(f"{BASE_URL}{endpoint}")
            data = response.json()

            for elt in data:
                try:
                    if key == "csnj":
                        coord_gps = elt["coordonnees_gps"].replace("N", "").replace("E", "").replace("S", "").replace("W", "").replace("/", "").replace(",", ".")
                        latitude, longitude = map(float, coord_gps.split())
                    elif key == "enseignement_superieur":
                        geo = elt.get("Géolocalisation", "").strip()
                        if geo:
                            latitude, longitude = map(float, geo.replace(" ", "").replace(",", " ").split())
                        else:
                            print(f"No geolocation available for: {elt}")
                            continue
                    else:
                        latitude, longitude = float(elt.get("Latitude", elt.get("Ylat", elt.get("Y_WGS84")))), float(elt.get("Longitude", elt.get("Xlong", elt.get("X_WGS84"))))

                    folium.Marker(
                        location=[latitude, longitude],
                        popup=f"{elt}",
                        icon=folium.Icon(color=color)
                    ).add_to(marker_cluster)
                except Exception as e:
                    print(f"Error processing element {elt}: {e}")
        except requests.RequestException as e:
            print(f"Error fetching data from endpoint {endpoint}: {e}")

    my_map.save("all.html")
    
if __name__ == "__main__":
    combined_map()