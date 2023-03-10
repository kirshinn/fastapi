import uvicorn
from fastapi import FastAPI
from pathlib import Path
from db.base import database

app = FastAPI(title="FastAPI Base")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    # uvicorn.run(f"{Path(__file__).stem}:app", host="127.0.0.1", port=8888, reload=True)
    pass
