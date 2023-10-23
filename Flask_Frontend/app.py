from flask import Flask, render_template, Response, stream_with_context
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('counter.html')

@app.route('/counter-increment')
def counter_increment():
    def generate():
        count = 1
        while count <= 20:
            time.sleep(1)
            yield f"data: {count}\n\n"
            count += 1
    return Response(stream_with_context(generate()), content_type='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
