from tkinter import *
from tkinter import ttk
from mandelbrot import draw_mandelbrot
from PIL import ImageTk, Image

WIDTH = 800
HEIGHT = 600
REVOLUTIONS = 100
ZOOM = 0.01

root = Tk()
root.title("Mandelbrot")
root.resizable(False,False)

tmp_img = draw_mandelbrot((WIDTH, HEIGHT), REVOLUTIONS, ZOOM)
img = ImageTk.PhotoImage(tmp_img)
label = Label(root, image=img)
label.pack()


def zoom_on_click(eventorigin):
    x = eventorigin.x
    y = eventorigin.y
    global ZOOM
    ZOOM *= 0.5
    tmp_img = draw_mandelbrot((WIDTH, HEIGHT), REVOLUTIONS, ZOOM)
    img = ImageTk.PhotoImage(tmp_img)
    label.configure(image=img)
    label.image = img


label.bind("<Button 1>", zoom_on_click)

root.mainloop()