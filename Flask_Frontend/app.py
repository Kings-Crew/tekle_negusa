from flask import Flask, render_template
import requests
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    response = requests.get("http://127.0.0.1:8000/allsensor/")  # Fetch all sensor data
    if response.status_code == 200:
        data = response.json()
        count = len(data)  # Count the number of data points
        return render_template('counter.html', count=count)  # Pass the count to the template
    else:
        return render_template('error.html', error="Failed to fetch data from the FastAPI endpoint")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
