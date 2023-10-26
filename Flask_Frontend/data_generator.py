from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import time

# Creating an instance of FastAPI, the main entry point for the API.
app = FastAPI()

origins = [
    "http://localhost:5000",  # Allow frontend domain
    "http://127.0.0.1:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Defining a route for the GET request to '/db/api/endpoint'.
@app.get('/db/api/endpoint')
def syntethic_data():
    var = 0
    # Running a loop for a random number of iterations between 1 and 10.
    for _ in range(random.randint(1, 5)):
         # Pausing the execution for a random number of seconds between 1 and 10.
        time.sleep(random.randint(1, 5))
        var += 1
    return {"data": var}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Changed port to 8000
