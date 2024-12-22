from fastapi import FastAPI, HTTPException, Path, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Annotated
from fastapi import FastAPI
from routers import task, user

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []

templates = Jinja2Templates(directory="templates")


@app.get("/")
def root():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)