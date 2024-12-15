from fastapi import FastAPI
from typing import Optional

app = FastAPI()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("module_16_1:app")

@app.get("/")
def read_main():
    return "Главная страница"

@app.get("/user/admin")
def admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
def user_page(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user")
def user_info(username: Optional[str] = None, age: Optional[int] = None):
    if username and age:
        return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
    elif username:
        return f"Информация о пользователе. Имя: {username}"
    return "Информация о пользователе не указана"
