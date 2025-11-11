import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Firebase
# We only need credentials, no storage bucket!
try:
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred)
except ValueError as e:
    print(f"Firebase already initialized or config error: {e}")

# Create database client
# We can import 'db' into any file that needs it
db = firestore.client()

print("Firebase (Firestore-only) connected successfully!")