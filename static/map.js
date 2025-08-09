// Initial coordinates from backend
const START_LAT = 28.6139;
const START_LNG = 77.2090;

let map = L.map('map').setView([START_LAT, START_LNG], 15);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

let busIcon = L.icon({
    iconUrl: 'bus.png',
    iconSize: [40, 40],
});

let marker = L.marker([START_LAT, START_LNG], { icon: busIcon }).addTo(map);

function updateBusLocation() {
    fetch('http://127.0.0.1:5000/get_location')
        .then(response => response.json())
        .then(data => {
            marker.setLatLng([data.lat, data.lng]);
            map.panTo([data.lat, data.lng]);
            document.getElementById('last-update').textContent =
                new Date().toLocaleTimeString();
        })
        .catch(err => console.error(err));
}

// Fetch every 3 seconds
setInterval(updateBusLocation, 3000);
