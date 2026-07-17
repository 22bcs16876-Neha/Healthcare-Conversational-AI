from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client()

# Create a test document
doc_ref = db.collection("test").document("demo")

doc_ref.set({
    "message": "Firestore connection successful."
})

print("Firestore connection successful.")
