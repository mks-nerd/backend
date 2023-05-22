from urllib.parse import quote_plus

import mongoengine  # type: ignore
from fastapi import FastAPI

from src import auth, home


def create_app() -> FastAPI:
    app = FastAPI(title="mks-api", version="0.1")
    app.include_router(auth.router.auth_route)
    app.include_router(home.router.home_route)

    MONGODB_USER_NAME: str = quote_plus("mks")
    MONGODB_USER_PASSWORD: str = quote_plus("this_is_password")
    MONGODB_BACKEND_DATABASE_NAME: str = quote_plus("backend_data")
    MONGODB_HOST_NAME: str = "localhost"
    MONGODB_PORT: int = 27017
    MONGODB_AUTHENTICATION_SOURCE: str = "admin"

    mongoengine.connect(
        MONGODB_BACKEND_DATABASE_NAME,
        host=MONGODB_HOST_NAME,
        port=MONGODB_PORT,
        username=MONGODB_USER_NAME,
        password=MONGODB_USER_PASSWORD,
        authentication_source=MONGODB_AUTHENTICATION_SOURCE,
        uuidRepresentation="standard",
        alias="backend_data",
    )
    return app
