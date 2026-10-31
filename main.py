import tkinter as tk
from config import *
import controller 
from login_window import *
from register_window import *

def main():
    main_window = tk.Tk()
    main_window.title(AUTH_TITLE)
    main_window.geometry(f"{AUTH_WIDTH}x{AUTH_HEIGHT}")
    main_window.resizable(False,False)

    login_button = tk.Button(main_window, text="Логин", background='#c6c6c6', command=show_login_window)
    login_button.pack(pady=5)

    register_button = tk.Button(main_window, text="Регистрация", background='#c6c6c6', command=show_register_window)
    register_button.pack(pady=10)

    main_window.mainloop()

if __name__ == "__main__":
    main()
