# 🚌 College Bus Tracker

A web app to track the live location of college buses using **Flask** as the backend and **Leaflet.js** for displaying an interactive map.

---

## 📌 Features
- **Simulation Mode** – Bus `B1` automatically moves between Angamaly and Kalady.
- **Driver Panel** – Allows bus drivers to send live GPS coordinates to the server.
- **Student Panel** – Students can enter a bus number and see its live location on a map.
- **Map View** – Displays the bus icon updating every few seconds.

---

## 📂 Project Structure
```
project/
│
├── app.py                # Flask backend server
├── static/               # Frontend files served by Flask
│   ├── index.html         # Home page (Driver / Student selection)
│   ├── driver.html        # Driver panel to send location updates
│   ├── student.html       # Student panel to search for a bus
│   ├── location.html      # Map view for a specific bus
│   ├── style.css          # Styling
│   ├── bus.png            # Bus icon
│
└── README.md              # This file
```

---

## 🚀 Getting Started

### 1️⃣ Install dependencies
Make sure Python 3 is installed, then:
```bash
pip install flask flask-cors
```

---

### 2️⃣ Run the Flask backend
```bash
python app.py
```
By default, Flask runs on:
```
http://127.0.0.1:5000
```

---

### 3️⃣ Open the app in your browser
Visit:
```
http://127.0.0.1:5000
```
You should see the **home page** with options for **Driver** and **Student**.

---

## 🧪 Simulation Mode (Testing)
- The backend automatically simulates bus **B1** moving between two points.
- To see it in action:
  1. Open `student.html`
  2. Enter `B1`
  3. Click **Show Location**  
     → This redirects to `location.html?bus=B1` where the map updates every 3 seconds.

---

## 📡 Real GPS Tracking
- Open `driver.html` on a phone or device with GPS.
- Enter your bus number and click **Start Tracking**.
- Your GPS location will be sent to the server every 5 seconds.

---

## 🔧 Important Notes
- All HTML, CSS, and images must be placed in the **`static/`** folder so Flask can serve them.
- When fetching from the backend, always use:
  ```
  http://127.0.0.1:5000/get_location/<bus_number>
  ```
- Bus numbers are **case-insensitive** if you modify `app.py` to handle that.

---

## 📜 License
This project is open-source and free to use.
