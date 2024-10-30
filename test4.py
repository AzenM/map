import requests
import folium
from folium.plugins import MarkerCluster
from pymongo import MongoClient, server_api
from pymongo.errors import ServerSelectionTimeoutError, PyMongoError

uri = "mongodb+srv://yeuu3u3u3u3:2ENRkpL8co0goYUv@cluster0.nqu2uzh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&tls=true&tlsAllowInvalidCertificates=true"
client = MongoClient(uri, server_api=server_api.ServerApi('1'), maxPoolSize=50, serverSelectionTimeoutMS=30000)

try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB")
except ServerSelectionTimeoutError as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)

COLORS = ["red", "blue", "green", "purple", "orange", "darkred", "lightred", "beige", "darkblue", "darkgreen", "cadetblue", "pink", "lightblue"]

def generate_gouv_stops_map():
    collection = client["Data"]["Gouv"]
    try:
        documents = list(collection.find())
        if not documents:
            print("No documents found in the collection.")
            return
    except PyMongoError as e:
        print(f"Error fetching documents: {e}")
        return

    map_center = [46.603354, 1.888334]
    my_map = folium.Map(location=map_center, zoom_start=6)
    marker_cluster = MarkerCluster().add_to(my_map)

    for document in documents:
        try:
            latitude = float(document.get("latitude"))
            longitude = float(document.get("longitude"))
            lib_fs = document.get("lib_fs", "Unknown Service")
            adresse = document.get("adresse", "Unknown Address")
            telephone = document.get("telephone", "Unknown Phone")

            popup_content = (
                f"Service: {lib_fs}<br>"
                f"Address: {adresse}<br>"
                f"Telephone: {telephone}<br>"
                f"Stop ID: {document.get('_id')}"
            )

            folium.Marker(
                location=[latitude, longitude],
                popup=popup_content,
                icon=folium.Icon(color="blue")
            ).add_to(marker_cluster)
        except Exception as e:
            print(f"Error processing document {document}: {e}")

    my_map.save("gouv_stops_map.html")

if __name__ == "__main__":
    generate_gouv_stops_map()
