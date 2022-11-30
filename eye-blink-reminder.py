from tkinter import *
from PIL import ImageTk, Image
import time


def eye():
    # Create an instance of tkinter window
    win = Tk()

    # Define the geometry of the window
    win.geometry("30x30")
    win.overrideredirect(True)

    frame = Frame(win, width=30, height=30)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("eye.png").resize((30, 30), Image.Resampling.LANCZOS))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image=img)
    label.pack()

    window_height = 30
    window_width = 30

    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))

    win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    win.after(3000, lambda: win.destroy())
    win.mainloop()


while True:
    eye()
    time.sleep(5)

