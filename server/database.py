#Frontend

from fastapi import FastAPI

app = FastAPI()
 
@app.get("/", tags=["Root"]) #Identifierare (tags=["Root"]) används för att gruppera vägar. Vägar med samma taggar grupperas i ett avsnitt i API-dokumentationen.
async def root (): #root() eller read_root()?
  return {"message": "Hello World!"} #Här ska data som lagras i databasen visas, data från sensorn.



































