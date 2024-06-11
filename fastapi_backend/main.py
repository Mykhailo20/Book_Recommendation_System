from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import user, book, rating
from utils.auth import authentication
from config.data_config import lifespan


app = FastAPI(lifespan=lifespan)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(book.router)
app.include_router(rating.router)


@app.get("/")
def index():
    print(f"main.index")
    return {
        "data": "Hello, World!"
    }


# Allow local React application
origins = [
    'http://localhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, # allow authorization operations (log in and log out)
    allow_methods=["*"],
    allow_headers=["*"]
)