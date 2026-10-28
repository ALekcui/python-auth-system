import user_repository
import err_window

user = ...

def auth()->None:
    print(f"Привет - {user}")
    
def deny()->None:
    err_window.ShowError("Accses deny", "Неправильный логин или пароль. Пожалуйста проверьте написание логина и пароля и повторите попытку.")

def auth_user(login:str,password:str)->None:
    user = user_repository.get_user_by_login(login.strip())
    if user is None: deny()
    else: 
        if user.check_password(password.strip()): 
            auth()
        else: deny()