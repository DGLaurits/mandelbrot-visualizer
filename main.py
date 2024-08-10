from tkinter import *
from tkinter import ttk
from mandelbrot import create_mandelbrot
from PIL import ImageTk, Image

WIDTH = 800
HEIGHT = 600
REVOLUTIONS = 100
ZOOM = 0.01

def zoom_on_click(eventorigin):
    x = eventorigin.x
    y = eventorigin.y
    global ZOOM
    ZOOM *= 0.5
    draw_mandelbrot()

def draw_mandelbrot():
    tmp_img = create_mandelbrot((WIDTH, HEIGHT), REVOLUTIONS, ZOOM)
    img = ImageTk.PhotoImage(tmp_img)
    label.configure(image=img)
    label.image = img

root = Tk()
root.title("Mandelbrot")
root.resizable(False,False)

label = Label(root)
label.pack()

draw_mandelbrot()


label.bind("<Button 1>", zoom_on_click)

root.mainloop()