import uvicorn

if __name__ == "__main__":
    uvicorn.run("Mongodatabase.server.appAPI:app", host="0.0.0.0", port=8000, reload=True) #server.appAPI:app motsvarar mappen server, appAPI motsvarar appAPI.py och ":app" motsvarar instansen skapad för FastAPI. #host="0.0.0.0" motsvarar localhost.