import user_repository
import err_window
from config import *

def auth()->None:
    print(f"Привет - {current_user}")
    
def deny()->None:
    err_window.ShowError("Accses deny", "Неправильный логин или пароль. Пожалуйста проверьте написание логина и пароля и повторите попытку.", True)

def auth_user(login:str,password:str)->None:
    current_user = user_repository.get_user_by_login(login.strip())
    if current_user is None: deny()
    else: 
        if current_user.check_password(password.strip()): 
            auth()
        else: deny()