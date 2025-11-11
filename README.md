# Hydro Sense API

**Hydro Sense** is a water quality monitoring system backend built with Python and Flask. It serves as the central API for receiving, storing, and retrieving sensor data from IoT devices.

This project is submitted in partial fulfillment of the requirements for the Software Engineering course for 3rd Year BS in Information Technology students at the University of Science and Technology of Southern Philippines (USTP).

---

## 📋 Table of Contents
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [System Architecture](#-system-architecture)
- [API Endpoints](#-api-endpoints)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
- [Project Structure](#-project-structure)
- [Authors](#-authors)

---

## ✨ Features

- **Sensor Data Ingestion**: Accepts JSON payloads with water quality metrics.
- **Real-time Data Storage**: Stores sensor readings in a scalable NoSQL database (Google Firestore).
- **Timestamping**: Automatically adds a UTC timestamp for every reading received.
- **Data Retrieval**: Provides a flexible API endpoint to fetch historical sensor data.
- **Scalable & Lightweight**: Built with Flask, making it efficient and easy to deploy.

---

## 🛠️ Technology Stack

- **Backend**: Python
- **Framework**: Flask
- **Database**: Google Cloud Firestore
- **CORS Handling**: Flask-CORS
- **Environment Management**: python-dotenv

---

## 🏗️ System Architecture

The system is designed around a simple, effective architecture:

1.  **IoT Device (e.g., Raspberry Pi)**: Reads data from various water sensors (pH, temperature, TDS, turbidity).
2.  **Data Transmission**: The IoT device sends the collected data as a JSON object to the Flask API.
3.  **Flask API Backend**:
    - Receives the data via a `POST` request.
    - Adds a server-side timestamp.
    - Connects to Google Firestore and stores the data in the `sensor_readings` collection.
4.  **Frontend Application**:
    - Fetches historical data from the API using a `GET` request to display charts, graphs, or tables.

---

## 🔌 API Endpoints

### 1. Receive Sensor Data

- **Endpoint**: `POST /api/sensor-data`
- **Description**: Receives a JSON object containing sensor readings and stores it in the database.
- **Request Body (JSON)**:
  ```json
  {
    "pi_id": "raspi-001",
    "ph": 7.5,
    "temperature": 26.1,
    "tds": 480,
    "turbidity": 22.5
  }
  ```
- **Success Response (201)**:
  ```json
  {
    "success": true,
    "data_received": {
      "pi_id": "raspi-001",
      "ph": 7.5,
      "temperature": 26.1,
      "tds": 480,
      "turbidity": 22.5,
      "timestamp": "2025-11-10T12:30:00.123456Z"
    }
  }
  ```

### 2. Get All Sensor Data

- **Endpoint**: `GET /api/sensor-data`
- **Description**: Retrieves a list of the most recent sensor readings.
- **Query Parameters**:
  - `limit` (optional): Number of records to return. Defaults to `20`. Maximum is `100`.
  - **Example**: `/api/sensor-data?limit=5`
- **Success Response (200)**:
  ```json
  [
    {
      "id": "documentId1",
      "pi_id": "raspi-001",
      "ph": 7.5,
      "temperature": 26.1,
      "tds": 480,
      "turbidity": 22.5,
      "timestamp": "2025-11-10T12:30:00.123456Z"
    },
    {
      "id": "documentId2",
      "pi_id": "raspi-001",
      "ph": 7.6,
      "temperature": 26.0,
      "tds": 482,
      "turbidity": 22.9,
      "timestamp": "2025-11-10T12:25:00.987654Z"
    }
  ]
  ```

---

## 🚀 Getting Started

Follow these instructions to get the API server running on your local machine.

### Prerequisites

- Python 3.8+
- A Google Cloud Platform (GCP) project with Firestore enabled.
- GCP authentication credentials (a service account JSON file).

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd Hydrosense
    ```

2.  **Create a virtual environment and activate it:**
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    *(You should create a `requirements.txt` file for this)*
    ```sh
    pip install Flask Flask-Cors firebase-admin python-dotenv
    ```

4.  **Set up Firebase credentials:**
    - Download your service account key file from your GCP project.
    - Set an environment variable that points to your key file.
    ```sh
    # For Windows (in Command Prompt)
    setx GOOGLE_APPLICATION_CREDENTIALS "C:\path\to\your\keyfile.json"

    # For macOS/Linux
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/keyfile.json"
    ```
    *Note: You may need to restart your terminal for the variable to be recognized.*

5.  **Run the application:**
    ```sh
    python app.py
    ```
    The API will be running at `http://127.0.0.1:5000`.

---

## 📂 Project Structure

```
Hydrosense/
├── .env             # (Optional) For environment variables
├── app.py           # Main Flask application file
├── firebase_config.py # Firebase initialization logic
├── requirements.txt # Project dependencies
└── venv/            # Python virtual environment
```

---

## 🧑‍💻 Authors

This project was developed by:

- *Edimar Mosquida*
- *Sean Paul De Guzman*
- *John Vincent Nogas*
- *Kyle Raterta*

**University of Science and Technology of Southern Philippines**
**College of Information Technology and Computing**
**A.Y. 2025-2026**