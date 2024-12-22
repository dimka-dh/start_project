from Module_17.m17_2.backend.db import Base, engine
from Module_17.m17_2.models import User, Task
from sqlalchemy.schema import CreateTable
from fastapi import FastAPI
from routers import task, user

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)

print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
