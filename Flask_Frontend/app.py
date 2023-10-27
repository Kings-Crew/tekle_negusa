# Import necessary modules from Flask.
from flask import Flask, render_template, Response, stream_with_context

# Import the requests module to make HTTP requests.
import requests

# Import CORS from flask_cors to handle cross-origin requests.
from flask_cors import CORS

# Initialize the Flask application.
app = Flask(__name__)

# Setup CORS for the Flask app. This allows the frontend running on "http://127.0.0.1:5000" 
# to make requests to this backend without facing cross-origin issues.
CORS(app, resources={r"/counter-increment": {"origins": "http://127.0.0.1:5000"}})

# Define the root route. When a user accesses the root URL ("/"), 
# the "counter.html" template will be rendered.
@app.route('/')
def index():
    return render_template('counter.html')

# Define the "/counter-increment" route. This route streams data to the frontend.
@app.route('/counter-increment')
def counter_increment():
    
    # This is a generator function. It fetches data from the FastAPI endpoint and 
    # then yields (sends) that data in the format expected by Server-Sent Events (SSE).
    def generate():
        # Make an HTTP GET request to the FastAPI endpoint.
        response = requests.get("http://127.0.0.1:8000/db/api/endpoint")
        
        # Parse the JSON response from the FastAPI endpoint.
        data = response.json()
        
        # Yield the data in the SSE format.
        yield f"data: {data['data']}"

    # Return the streamed response. The stream_with_context function ensures 
    # that the app can stream data without losing the context.
    return Response(stream_with_context(generate()), content_type='text/event-stream')

# If this script is being run directly (as opposed to being imported), 
# start the Flask development server.
if __name__ == "__main__":
    app.run(debug=True, threaded=True)
