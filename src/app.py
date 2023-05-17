from urllib.parse import quote_plus

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel
import mongoengine  # type: ignore

from src.models import User as UserMongo  # type: ignore
from src.home.router import home_route

MONGO_USER_ID: str = quote_plus("mks")
MONGO_USER_PASSWORD: str = quote_plus("this_is_password")
DATABASE_NAME: str = quote_plus("backend-data")
HOST_NAME: str = "localhost"
MONGO_PORT: int = 27017

app = FastAPI()
app.include_router(home_route)
client = TestClient(app)

mongoengine.connect(
    host=f"mongodb://{MONGO_USER_ID}:{MONGO_USER_PASSWORD}@localhost:27017/{DATABASE_NAME}?authSource=admin",
    uuidRepresentation="standard",
)


class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    likes: list[str]


@app.get("/")
def greet():
    return {"msg": "hello"}


@app.post("/add_user")
def add_user(user: User):
    # return dict(user)
    UserMongo(**dict(user)).save()
    return user


@app.post("/remove_user")
def remove_user(user: User):
    UserMongo.objects(**dict(user)).delete()
    return user
