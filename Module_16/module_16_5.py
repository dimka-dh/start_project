from fastapi import FastAPI, HTTPException, Path, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []

templates = Jinja2Templates(directory="templates")


@app.get("/")
def get_all_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users, "user": None})


@app.get("/user/{user_id}")
def get_user_by_id(
        request: Request,
        user_id: Annotated[int,
        Path(
            title="Введите ID пользователя",
            description="Уникальный идентификатор пользователя",
            example=1
        )
        ]
):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="Пользователь не найден")


@app.post("/user/{username}/{age}")
def add_user(
        username: Annotated[str,
        Path(
            title="Введите имя пользователя",
            description="Имя пользователя (от 5 до 20 символов)",
            min_length=5, max_length=20,
            example="София"
        )
        ],
        age: Annotated[int,
        Path(
            title="Введите возраст пользователя",
            description="Возраст пользователя (от 18 до 120 лет)",
            ge=18, le=120,
            example=27
        )
        ]
):
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
def update_user(
        user_id: Annotated[int,
        Path(
            title="Введите ID пользователя",
            description="ID пользователя",
            example=1
        )
        ],
        username: Annotated[str,
        Path(
            title="Введите имя пользователя",
            description="Имя пользователя (от 5 до 20 символов)",
            min_length=5, max_length=20,
            example="София"
        )
        ],
        age: Annotated[int,
        Path(
            title="Введите возраст пользователя",
            description="Возраст пользователя (от 18 до 120 лет)",
            ge=18, le=120, example=28
        )
        ]
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")


@app.delete("/user/{user_id}")
def delete_user(
        user_id: Annotated[int,
        Path(
            title="Введите ID пользователя",
            description="ID пользователя для удаления",
            example=2
        )
        ]
):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("module_16_5:app", reload=True)
