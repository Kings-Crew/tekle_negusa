from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime
import uuid

app = Flask(__name__)

# Anslut till MongoDB
client = MongoClient('mongodb://localhost', 27017)
db = client['person_database']
collection = db['people']

@app.route('/personDetected', methods=['POST'])
def person_detected():
    # Skapa ett unikt ID och tidsstämpel
    person_id = str(uuid.uuid4())
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        # Lägg till i MongoDB
        collection.insert_one({"id": person_id, "timestamp": timestamp})
        print(f"Adding person with ID: {person_id} at {timestamp}")
        print("Received POST request")
        
        return "Person added successfully", 200
    except Exception as e:
        print(e)
        return "Error adding person", 500
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
