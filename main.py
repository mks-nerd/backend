import uvicorn

from src.app import app

if __name__ == "__main__":
    uvicorn.run(app=app)
