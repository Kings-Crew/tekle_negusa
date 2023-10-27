# Import necessary modules from FastAPI, as well as the random and time modules.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import time

# Instantiate the FastAPI application.
app = FastAPI()

# Define a list of origins (frontends) that are allowed to access this backend.
# In this case, it's the frontend running on "http://localhost:5000" and "http://127.0.0.1:5000".
origins = [
    "http://localhost:5000",
    "http://127.0.0.1:5000",
]

# Add CORS (Cross-Origin Resource Sharing) middleware to the FastAPI application.
# This setup allows the listed origins to make requests to this backend 
# without facing cross-origin issues.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a route for the GET request to '/db/api/endpoint'.
@app.get('/db/api/endpoint')
def syntethic_data():
    var = 0
    # Run a loop for a random number of iterations between 1 and 5.
    for _ in range(random.randint(1, 5)):
        # Pause the execution for a random duration between 1 and 5 seconds.
        time.sleep(random.randint(1, 5))
        var += 1  # Increment the 'var' for each iteration.
    return {"data": var}  # Return the final value of 'var' as a JSON response.

# If this script is being run directly (as opposed to being imported), 
# start the FastAPI development server using Uvicorn.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Start the server on port 8000.
