from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = [
    "http://localhost:5000",
    "http://127.0.0.1:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/db/api/endpoint')
def syntethic_data():
    with open('posts.json', 'r') as file:  # Open the JSON file.
        posts = json.load(file)  # Load the JSON content.
    number_of_posts = len(posts["posts"])  # Count the number of posts.
    return {"data": number_of_posts}  # Return the count as data.

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
