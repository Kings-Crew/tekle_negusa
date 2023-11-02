from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

fastapi_app = FastAPI()

origins = [
    "http://localhost:5000",
    "http://127.0.0.1:5000",
]

fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@fastapi_app.get('allsensors')
def syntethic_data():
    with open('posts.json', 'r') as file:  # Open the JSON file.
        posts = json.load(file)  # Load the JSON content.
    number_of_posts = len(posts["posts"])  # Count the number of posts.
    return {"data": number_of_posts}  # Return the count as data.

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)
