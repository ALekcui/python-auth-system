import tkinter as tk
from config import *
from PIL import Image, ImageTk

def ShowError(ErrorName: str, ErrorText: str, withImage: bool) -> None:
    
    Error_Window = tk.Toplevel()
    Error_Window.geometry(f"{ERROR_WIDTH} x {ERROR_HEIGHT}")
    Error_Window.resizable(False, False)
    Error_Window.configure(background='white')
    Error_Window.title(ErrorName)

    BottomPannel = tk.Frame(Error_Window, bg='#f0f0f0', height=ERROR_HEIGHT / 4)
    BottomPannel.pack(side='bottom', fill='x')
    BottomPannel.pack_propagate(False)
    
    if withImage:
        try:
            image = Image.open("Иди нахуйСФ.jpg") 
            image.thumbnail((ERROR_WIDTH-ERROR_WIDTH / 4, ERROR_HEIGHT-ERROR_HEIGHT / 4))
            photo = ImageTk.PhotoImage(image)
            
            LeftPannel = tk.Frame(Error_Window, background='#ffffff', width=ERROR_WIDTH-ERROR_WIDTH / 4, height=ERROR_HEIGHT-ERROR_HEIGHT / 4)
            LeftPannel.pack(side='left')
            
            canvas = tk.Canvas(LeftPannel, width=image.width, height=image.height, background='#ffffff')
            canvas.pack(side='left')
            canvas.create_image(0, 0, image=photo, anchor='nw')
            
        except FileNotFoundError:
            print("Ошибка: Файл изображения 'Иди нахуйСФ.jpg' не найден")
            withImage = False

    Text = tk.Label(Error_Window, text=ErrorText, wraplength=((int(ERROR_WIDTH - image.width - 15)) if withImage else (ERROR_WIDTH-15)), justify='left', background='#ffffff')
    Text.pack(padx=5, pady=15, side='left', anchor='n', expand=True)
    
    ok_button = tk.Button(BottomPannel, text=("Уже бегу!" if withImage else "OK"), width=10, height=1, command=Error_Window.destroy, background='#ffffff')
    ok_button.pack(side='right', pady=(int(BottomPannel.cget('height'))/8), padx=ERROR_WIDTH/24)

    Error_Window.mainloop()

if __name__ == "__main__":
    ShowError("Test", "Неправильный логин или пароль. Пожалуйста проверьте написание логина и пароля и повторите попытку.", True)
