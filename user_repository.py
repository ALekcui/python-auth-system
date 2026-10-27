from User import User
users = [
    User("Старый бог","wind_of_changes","Вовчик Адидас"),
    User("Chill Guy", "12345","Чиловый Парень"),
    User("ALekcui","123pass","Алексей Гордиевский"),
    User("Kirill","paravozik12345","Кирилл Паравозов"),
    User("sigma","sigmaBOY","Жгуев Реев"),
    User("BlackWhite", "terraria123", "Кирилл Чёрный"),
    User("Pop cat", "pizdoxryak", "Кирил Писюнов"),
    User("vkidus", "pisunF6", "Кирилл Джигурда"),
    User("AlexDep", "Meow52", "Алекс Депай")
]
users_repos = {user.get_login(): user for user in users}
def get_user_by_login(login):
    return users_repos.get(login)
