from fastapi import APIRouter
from pydantic import BaseModel

from .models import HomePage


class MenuSchema(BaseModel):
    name: str
    endpoint: str


class HomePageSchema(BaseModel):
    name: str
    menu: list[MenuSchema]


home_route = APIRouter(prefix="/home")


@home_route.get("/get_home")
def get_home(home_name: str):
    data = [
        HomePageSchema(**obj.to_mongo()).dict()
        for obj in HomePage.objects(name=home_name)
    ]
    return data


@home_route.post("/add_home")
def add_home(home: HomePageSchema):
    HomePage(**home.dict()).save()
    return home


@home_route.post("/delete_home")
def delete_home():
    HomePage.objects.delete()
    return "success"
