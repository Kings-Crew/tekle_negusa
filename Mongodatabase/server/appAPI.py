#Api anslutningar/endpoints

import collections
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from typing import Collection, List
from pydantic import BaseModel
from urllib import request

#from server.models.validator_sensor import sensorschema
from server.routes.sensor import validate_json, schema
from mongodbase import TNcollection


app = FastAPI()

#utkommenterad pga test
#@app.get("/", tags=["Root"]) #Identifierare (tags=["Root"]) används för att gruppera vägar. Vägar med samma taggar grupperas i ett avsnitt i API-dokumentationen.
#async def root (): #root() eller read_root()?
#  return {"message": "Hello World!"} #Här ska data som lagras i databasen visas, data från sensorn.


# POST-endpoint för att ta emot och lagra data från sensorn
@app.post("/sensor/")
async def add_sensor_data(data: sensorschema):
    if validate_json(data.dict(), schema):
        TNcollection.insert_one(data.dict())
        return {"message": "Data inserted successfully."}
    else:
        raise HTTPException(status_code=400, detail="Data insertion failed due to validation error.")


# GET-endpoint för att hämta alla sensorposter
@app.get("/allsensor/", response_model=List[sensorschema])
async def get_all_data():
    data = list(TNcollection.find({}, {'_id': False}))
    return data


# GET-endpoint för att hämta en specifik sensorpost baserat på ID
@app.get("/sensor/{sensor_id}", response_model=sensorschema)
async def get_data_by_id(sensor_id: str):
    data = TNcollection.find_one({"id": sensor_id}, {'_id': False})
    if data:
        return data
    else:
        raise HTTPException(status_code=404, detail="Data not found.")

