import tkinter as tk
from config import *
import controller 

main_window = tk.Tk()
main_window.title(TITLE)
main_window.geometry(f"{WIDTH}x{HEIGHT}")

tk.Label(main_window, text="Логин").pack()
login_text = tk.Text(main_window,width=15, height=1)
login_text.pack()

tk.Label(main_window, text="Пароль").pack()
password_text = tk.Text(main_window, width=15, height=1)
password_text.pack()

auth_button = tk.Button(main_window, text="Войти", command=lambda: controller.auth_user(login_text.get(1.0, tk.END), password_text.get(1.0, tk.END)))
auth_button.pack()

if __name__ == "__main__":
    main_window.mainloop()