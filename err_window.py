import tkinter as tk
from config import *
from PIL import Image, ImageTk


def ShowError(ErrorName: str, ErrorText: str) -> None:
    Error_Window = tk.Toplevel()
    Error_Window.geometry(f"{ERROR_WIDTH}x{ERROR_HEIGHT}")
    Error_Window.resizable(False, False)
    Error_Window.configure(background='white')
    Error_Window.title(ErrorName)

    BottomPannel = tk.Frame(Error_Window, bg='#f0f0f0', height=ERROR_HEIGHT/4)
    BottomPannel.pack(side='bottom', fill='x')
    BottomPannel.pack_propagate(False)
    
    try:
        image = Image.open("Иди нахуйСФ.jpg") 
        image.thumbnail((ERROR_WIDTH-ERROR_WIDTH/4, ERROR_HEIGHT-ERROR_HEIGHT/4 ))
        photo = ImageTk.PhotoImage(image)
        
        
        LeftPannel = tk.Frame(Error_Window, background='#ffffff', width=ERROR_WIDTH-ERROR_WIDTH/4,height=ERROR_HEIGHT-ERROR_HEIGHT/4)
        LeftPannel.pack(side='left')
        
        canvas = tk.Canvas(LeftPannel, width=image.width, height=image.height, background='#ffffff')
        canvas.pack(side='left')
        canvas.create_image(0, 0, image=photo, anchor='nw')
        
        tk.Label(Error_Window, text=ErrorText, wraplength=int(ERROR_WIDTH - (image.width) - 15), justify='left', background='white').pack(padx=5, pady=15, side='left', anchor='nw', fill='both', expand=True)
        
        ok_button = tk.Button(BottomPannel, text="Уже бегу!", width=10, height=1, command=Error_Window.destroy)
        ok_button.pack(side='right', pady=(int(BottomPannel.cget('height'))/8), padx=ERROR_WIDTH/24)
    except FileNotFoundError:
        print("Ошибка: Файл изображения 'Иди нахуйСФ.jpg' не найден")

        tk.Label(Error_Window, text=ErrorText, wraplength=ERROR_WIDTH-15, justify='left', background='#ffffff').pack(padx=15,pady=15,side='top',anchor='w')
        
        ok_button = tk.Button(BottomPannel, text="OK", width=10, height=1, command=Error_Window.destroy, background='#ffffff')
        ok_button.pack(side='right', pady=(int(BottomPannel.cget('height'))/8), padx=ERROR_WIDTH/24)

    Error_Window.mainloop()

if __name__ == "__main__":
    ShowError(None, None)