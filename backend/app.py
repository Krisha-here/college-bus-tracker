from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import math
import os

app = Flask(__name__, static_folder="static")
CORS(app)

# Store bus locations in memory
bus_locations = {}

# Simulation: Angamaly -> Kalady
start_lat, start_lng = 10.1900, 76.3879
end_lat, end_lng = 10.1540, 76.4760

# Start position for our example bus "B1"
bus_locations["B1"] = (start_lat, start_lng)

# Step size per update (degrees)
STEP = 0.0008  # smaller = slower movement

def move_towards(lat1, lng1, lat2, lng2, step):
    """Move from (lat1, lng1) towards (lat2, lng2) by 'step' distance."""
    dist = math.sqrt((lat2 - lat1) ** 2 + (lng2 - lng1) ** 2)
    if dist < step:
        return lat2, lng2  # reached destination
    ratio = step / dist
    new_lat = lat1 + (lat2 - lat1) * ratio
    new_lng = lng1 + (lng2 - lng1) * ratio
    return new_lat, new_lng

# Serve frontend
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

# API endpoint: update location manually
@app.route("/update_location", methods=["POST"])
def update_location():
    data = request.json
    bus_locations[data["bus_number"]] = (data["lat"], data["lon"])
    return "Location updated", 200

# API endpoint: get location (with simulation for B1)
@app.route("/get_location/<bus_number>")
def get_location(bus_number):
    if bus_number in bus_locations:
        lat, lon = bus_locations[bus_number]

        # If it's the simulated bus "B1", move it towards Kalady
        if bus_number == "B1":
            new_lat, new_lng = move_towards(lat, lon, end_lat, end_lng, STEP)
            bus_locations["B1"] = (new_lat, new_lng)

            # Loop back to start when reaching destination
            if round(new_lat, 5) == end_lat and round(new_lng, 5) == end_lng:
                bus_locations["B1"] = (start_lat, start_lng)

        return jsonify({"lat": bus_locations[bus_number][0], "lon": bus_locations[bus_number][1]})

    return jsonify({"error": "Bus not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
