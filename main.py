from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def get_main_page():
    return 'Главная страница'


@app.get("/user/admin")
async def get_admin_page():
    return 'Вы вошли как админ'


@app.get("/user/{user_id}")
async def get_user_number(user_id: int):
    return f'Вы вошли как пользователь №{user_id}'


@app.get("/user")
async def get_user_info(username: str = 'UrbanUser', age=24):
    return f'Информация о пользователе. Имя: {username},  Возраст: {age}'
