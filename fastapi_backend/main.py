from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session

from routers import user

app = FastAPI()

app.include_router(user.router)

@app.get("/")
def index():
    return {
        "data": "Hello, World!"
    }
