from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("module_16_4:app", reload=True)


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []


@app.get("/users")
def get_users():
    return users


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
            example="1"
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
            ge=18, le=120,
            example=27
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
        user_id: Annotated[
            int,
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
