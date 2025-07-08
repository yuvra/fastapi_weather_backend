import firebase_admin
from firebase_admin import credentials, firestore
from pathlib import Path

# Construct correct path relative to this file
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
cred_path = BASE_DIR / "firebase-service-account.json"

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate(str(cred_path))
    firebase_admin.initialize_app(cred)

db = firestore.client()
