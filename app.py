from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

# Import our (simplified) Firebase database client
from firebase_config import db

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Water Monitoring API is running!"

# --- Updated Endpoint: Receive ALL Sensor Data (JSON) ---
@app.route('/api/sensor-data', methods=['POST'])
def receive_sensor_data():
    """
    Receives JSON data from Raspberry Pi and stores it in Firestore.
    Now includes turbidity!
    
    Expected JSON:
    {
      "pi_id": "raspi-001",
      "ph": 8.1,
      "temperature": 25.5,
      "tds": 450,
      "turbidity": 25.2  <-- YOUR NEW NUMERICAL VALUE
    }
    """
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Add a server timestamp
        data['timestamp'] = datetime.datetime.now(datetime.timezone.utc)

        # Add data to Firestore
        # 'sensor_readings' is the name of your collection
        collection_ref = db.collection('sensor_readings')
        collection_ref.add(data)

        return jsonify({"success": True, "data_received": data}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

#
# WE HAVE DELETED THE /api/turbidity-image ENDPOINT
#

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)