import uvicorn

from ..backend.src.app import app # type: ignore

if __name__ == "__main__":
    uvicorn.run(app=app)
