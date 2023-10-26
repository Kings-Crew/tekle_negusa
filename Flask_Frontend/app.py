from flask import Flask, render_template, Response, stream_with_context
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/counter-increment": {"origins": "http://127.0.0.1:5000"}})

@app.route('/')
def index():
    return render_template('counter.html')

@app.route('/counter')
def counter_increment():
    def generate():
        # Fetch data from the FastAPI endpoint
        response = requests.get("http://127.0.0.1:8000/db/api/endpoint")
        data = response.json()
        yield f"data: {data['data']}\\n\\n"

    return Response(stream_with_context(generate()), content_type='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
