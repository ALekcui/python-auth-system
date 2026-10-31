from User import User
import os
import json
from config import *

defaul_users =[
            User("User1", "password", "Name Lastname"),
            User("User2", "password2","Name Lastname2"),
            User("Test User", "12345", "Test")
        ]

users = defaul_users

def load_users():
    global users

    if not os.path.exists(USERS):
        return defaul_users
    
    with open(USERS, "r", encoding="utf-8") as users:
        try:
            users = [User(user["login"], user["password"], user["fio"]) for user in (json.load(users))]
        except json.JSONDecodeError:
            users = defaul_users
            
load_users()

def save_users(users_list: list[str] ) -> None:
    data = []
    for user in users_list:
        data.append({
            "login": user.get_login(),
            "password": user._password,
            "fio": user.get_name()
        })
    
    with open(USERS, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if not os.path.exists(USERS):
    save_users(users)

users_repos = {user.get_login(): user for user in users}

def get_user_by_login(login: str):
    return users_repos.get(login)

def add_user(login:str, password: str, fio: str) -> bool:
    if login in users_repos:
        return False 
    
    new_user = User(login, password, fio)
    users.append(new_user)
    users_repos[login] = new_user
    
    save_users(users)
    return True
