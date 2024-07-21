from fastapi import FastAPI

from app import models
from app.api.api_v1.endpoints import user
from app.db.database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user.router, prefix="/users", tags=["users"])


@app.get('/')
def read_root():
    return {'Hello': 'World'}


if __name__ == "__main__":
    print("Hello World")
