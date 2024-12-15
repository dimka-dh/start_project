from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("module_16_2:app", reload=True)


@app.get("/")
def read_main():
    return "Главная страница"


@app.get("/user/admin")
def admin_page():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
def get_page(
        user_id: Annotated[int,
            Path(
                title="Введите ID пользователя",
                description="ID пользователя, который вы хотите получить",
                ge=1, le=100,
                example=1
            )
        ]
):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
def get_user_details(
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
    return {"message": f"Username: {username}, Age: {age}"}
