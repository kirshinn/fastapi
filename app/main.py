import uvicorn
from fastapi import FastAPI
from pathlib import Path

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(f"{Path(__file__).stem}:app", host="127.0.0.1", port=8888, reload=True)
    # pass
