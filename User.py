class User:
    def __init__(self,login,password,fio):
        self._login = login
        self._password = password
        self._fio = fio
    def check_password(self,password):
        return password == self._password
    def get_name(self):
        return self._fio
    def get_login(self):
        return self._login