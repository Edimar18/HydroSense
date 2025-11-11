from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
from firebase_admin import firestore

# Import our (simplified) Firebase database client
from firebase_config import db

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hydro Sense API is running!"

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

# --- New Endpoint: Get ALL Sensor Data (for Frontend) ---
@app.route('/api/sensor-data', methods=['GET'])
def get_sensor_data():
    """
    Retrieves historical sensor data from Firestore, ordered by most recent.
    Supports a 'limit' query parameter to control the number of results.
    Example: /api/sensor-data?limit=50
    """
    try:
        # Get the 'limit' query parameter, default to 20, with a max of 100
        limit = request.args.get('limit', 20, type=int)
        if limit > 100:
            limit = 100

        collection_ref = db.collection('sensor_readings')

        # Query the collection, order by timestamp descending, and limit results
        query = collection_ref.order_by(
            'timestamp', direction=firestore.Query.DESCENDING
        ).limit(limit)
        docs = query.stream()

        results = []
        for doc in docs:
            doc_data = doc.to_dict()
            doc_data['id'] = doc.id  # Include the document ID
            results.append(doc_data)

        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
#
# WE HAVE DELETED THE /api/turbidity-image ENDPOINT
#

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)