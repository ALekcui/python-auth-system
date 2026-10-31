import tkinter as tk
from config import *
import controller
from user_repository import load_users

def show_login_window():
    login_window = tk.Toplevel()
    login_window.geometry(f"{LOGIN_WIDTH}x{LOGIN_HEIGHT}")
    login_window.resizable(False, False)
    login_window.title("Login Window")

    tk.Label(login_window, text="Логин").pack()
    login_text = tk.Text(login_window,width=15, height=1, wrap=None)
    login_text.pack()

    tk.Label(login_window, text="Пароль").pack()
    password_text = tk.Text(login_window, width=15, height=1, wrap=None)
    password_text.pack()
    
    auth_button = tk.Button(login_window, text="Войти", background='#c6c6c6', command=lambda: controller.auth_user(login_text.get(1.0, tk.END), password_text.get(1.0, tk.END)))
    auth_button.pack(pady=5)

    load_users()

    login_window.mainloop()
