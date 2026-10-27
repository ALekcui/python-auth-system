from User import User
import os
import json


USERS = "users.json"

def load_users():
    if not os.path.exists(USERS):
        return [
            User("User1", "password", "Name Lastname"),
            User("Test User", "12345", "Test")
        ]
    
    with open(USERS, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return [User(u["login"], u["password"], u["fio"]) for u in data]
        except json.JSONDecodeError:
            return []

def save_users(users_list):
    data = []
    for user in users_list:
        data.append({
            "login": user.get_login(),
            "password": user._password,
            "fio": user.get_name()
        })
    
    with open(USERS, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

users = load_users()

if not os.path.exists(USERS):
    save_users(users)

users_repos = {user.get_login(): user for user in users}

def get_user_by_login(login):
    return users_repos.get(login)

def add_user(login, password, fio):
    if login in users_repos:
        return False 
    
    new_user = User(login, password, fio)
    users.append(new_user)
    users_repos[login] = new_user
    
    save_users(users)
    return True
