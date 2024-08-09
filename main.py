from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Mandelbrot")
root.geometry("600x400")

# Returns how many steps before the value escapes the circle with a radius of 2
def mandelbrot(c, revolutions):

    value = 0
    times = 0

    for _ in range(revolutions):
        if abs(c) >= 2:
            return times
        value = value*value
        times += 1

root.mainloop()