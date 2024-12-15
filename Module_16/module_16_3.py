from fastapi import FastAPI, HTTPException, Path
from typing import Annotated

app = FastAPI()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("module_16_3:app", reload=True)

users = {"1": "Имя: Example, возраст: 18"}


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
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"Пользователь с ID {new_id} создан"


@app.put("/user/{user_id}/{username}/{age}")
def update_user(
        user_id: Annotated[str,
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
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"Пользователь с ID {user_id} изменен"


@app.delete("/user/{user_id}")
def delete_user(
        user_id: Annotated[str,
        Path(
            title="Enter user ID",
            description="ID пользователя для удаления",
            example="2"
        )
        ]
):
    del users[user_id]
    return f"Пользователь с ID  {user_id}был удален"
