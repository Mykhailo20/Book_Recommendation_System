from fastapi import FastAPI

from routers import user, book, rating

app = FastAPI()

app.include_router(user.router)
app.include_router(book.router)
app.include_router(rating.router)

@app.get("/")
def index():
    print(f"main.index")
    return {
        "data": "Hello, World!"
    }