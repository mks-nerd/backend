from pydantic import BaseModel


class UserSchema(BaseModel):
    first_name: str
    last_name: str
    age: int
    likes: list[str]
