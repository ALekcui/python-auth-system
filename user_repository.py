from User import User
users = [
    User("User1","password","Name Lastname"),
    User("Test User","12345","Test")
]
users_repos = {user.get_login(): user for user in users}
def get_user_by_login(login):
    return users_repos.get(login)
