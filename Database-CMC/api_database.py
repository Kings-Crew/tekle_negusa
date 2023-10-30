#Api byggt med hjälp av FastAPI
#CMC står för: Control Management Center
from fastapi import FastAPI

app = FastAPI()
 
@app.get("/")
def root ():
  return {"message": "Hello World!"}
