from urllib.parse import quote_plus

import mongoengine  # type: ignore
from fastapi import FastAPI
from fastapi.testclient import TestClient

import src.home.models
from src import auth, home


def create_app(
    mongodb_host_name: str = "mongo", mongodb_port: int = 27017
) -> tuple[FastAPI, TestClient]:
    app = FastAPI(title="mks-api", version="0.1")
    app.include_router(auth.router.auth_route)
    app.include_router(home.router.home_route)
    client: TestClient = TestClient(app)

    MONGODB_USER_NAME: str = quote_plus("mks")
    MONGODB_USER_PASSWORD: str = quote_plus("this_is_password")
    MONGODB_BACKEND_DATABASE_NAME: str = quote_plus("backend_data")
    MONGODB_HOST_NAME: str = mongodb_host_name
    MONGODB_PORT: int = mongodb_port
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

    return app, client
