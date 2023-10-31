from flask import Flask, render_template
import requests
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    response = requests.get("http://127.0.0.1:8000/db/api/endpoint")
    if response.status_code == 200:
        data = response.json()
        return render_template('counter.html', element=data['data'])
    else:
        return render_template('error.html', error="Failed to fetch data from the FastAPI endpoint")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
