import tkinter as tk
from config import *
import controller

def show_register_window():
    register_window = tk.Toplevel()
    register_window.geometry(f"{REGISTER_WIDTH}x{REGISTER_HEIGHT}")
    register_window.resizable(False, False)
    register_window.title("Register Window")

    tk.Label(register_window, text="Новый логин").pack()
    new_login_text = tk.Text(register_window, width=15, height=1, wrap=None)
    new_login_text.pack()

    tk.Label(register_window, text="Пароль").pack()
    password_text = tk.Text(register_window, width=15, height=1, wrap=None)
    password_text.pack()

    tk.Label(register_window, text="Фио").pack()
    fio_text = tk.Text(register_window, width=15, height=1, wrap=None)
    fio_text.pack()

    reg_button = tk.Button(register_window, text="Зарегистрироваться", background='#c6c6c6', command=lambda: controller.reg_user(new_login_text.get(1.0, tk.END), password_text.get(1.0, tk.END), fio_text.get(1.0, tk.END)))
    reg_button.pack(pady=5)

    register_window.mainloop()
