#Api byggt med hjälp av FastAPI

from fastapi import FastAPI

app = FastAPI()
 
@app.get("/")
def root ():
  return {"message": "Hello World!"}
