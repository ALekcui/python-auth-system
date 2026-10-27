import user_repository
def auth_user(login,password):
    user = user_repository.get_user_by_login(login.strip())
    message:str="Доступ запрещён"
    if user is None:
        pass
    else:
        if user.check_password(password.strip()):
            message = f"Привет - {user.get_name()}"
    print(message)