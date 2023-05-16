from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI()
client = TestClient(app)


@app.get("/")
def greet():
    return {"msg": "hello"}
