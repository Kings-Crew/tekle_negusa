#databasanslutningsinformationen där man definierade anslutningsinformationen.

<<<<<<< HEAD:Mongodatabase/server/mongodbase.py
from dotenv import load_dotenv
import os
import pymongo
import dns

# Ladda variabler från .env-filen.
load_dotenv()

# Hämta och läs anslutningssträngen från .env
connection_string = os.getenv('connectionString')

# Anslut mot MongoDB-klient med den hämtade anslutningssträngen.
if connection_string:
    client = pymongo.MongoClient(connection_string)
else:
    print("No connection string provided.")

# Skapar en ny databas/om den är skapad tar den oss till denna database.
TNdatabase = client ["Sensor_Data"]

# Skapar en ny collection i vår databas "TNdatabase"/om den är skapad tar den oss till denna collection.
TNcollection = TNdatabase ["Collection_Sensor_Data"]

=======
>>>>>>> 676e3ef5f664e974c0f5304893fae8f74729a3a1:server/mongodbase.py
