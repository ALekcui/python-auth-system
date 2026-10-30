import tkinter as tk
from config import *
import controller 

main_window = tk.Tk()
main_window.title(AUTH_TITLE)
main_window.geometry(f"{AUTH_WIDTH}x{AUTH_HEIGHT}")
main_window.resizable(False,False)

tk.Label(main_window, text="Логин").pack()
login_text = tk.Text(main_window,width=15, height=1, wrap=None)
login_text.pack()

tk.Label(main_window, text="Пароль").pack()
password_text = tk.Text(main_window, width=15, height=1, wrap=None)
password_text.pack()

auth_button = tk.Button(main_window, text="Войти", background='#c6c6c6', command=lambda: controller.auth_user(login_text.get(1.0, tk.END), password_text.get(1.0, tk.END))).pack(pady=5)

if __name__ == "__main__":
    main_window.mainloop()