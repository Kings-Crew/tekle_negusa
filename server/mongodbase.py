#databasanslutningsinformationen där man definierade anslutningsinformationen.

from dotenv import load_dotenv
import os
import pymongo
import dns

# Ladda variabler från .env-filen
load_dotenv()

# Hämta och läs anslutningssträngen från .env
connection_string = os.getenv('connectionString')

# Anslut mot MongoDB-klient med den hämtade anslutningssträngen
if connection_string:
    client = pymongo.MongoClient(connection_string)
else:
    print("No connection string provided.")

