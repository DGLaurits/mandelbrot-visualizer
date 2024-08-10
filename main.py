from tkinter import *
from tkinter import ttk
from mandelbrot import draw_mandelbrot
from PIL import ImageTk, Image

WIDTH = 600
HEIGHT = 400
REVOLUTIONS = 100
ZOOM = 0.01

root = Tk()
root.title("Mandelbrot")

tmp_img = draw_mandelbrot((WIDTH, HEIGHT), REVOLUTIONS, ZOOM)
img = ImageTk.PhotoImage(tmp_img)
label = Label(image=img)
label.image = img
label.pack()


root.mainloop()