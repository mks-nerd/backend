from pydantic import BaseModel


class MenuSchema(BaseModel):
    name: str
    endpoint: str


class HomePageSchema(BaseModel):
    name: str
    menu: list[MenuSchema]
    about: str
    skills: list[str]
    hobbies: list[str]
