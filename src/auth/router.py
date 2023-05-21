from fastapi import APIRouter

from .models import User
from .schema import UserSchema

auth_route = APIRouter(prefix="/auth")


@auth_route.post("/add_user")
async def add_user(user: UserSchema):
    # return dict(user)
    User(**dict(user)).save()
    return user


@auth_route.post("/remove_user")
async def remove_user(user: UserSchema):
    User.objects(**dict(user)).delete()
    return user
