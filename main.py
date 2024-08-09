from tkinter import *
from tkinter import ttk

WIDTH = 600
HEIGHT = 400
REVOLUTIONS = 5
ZOOM = 0.1

root = Tk()
root.title("Mandelbrot")

canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg = "#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH//2, HEIGHT//2), image=img, state="normal")

# Returns how many steps before the value escapes the circle with a radius of 2
def mandelbrot(c, revolutions):

    c = complex(c[0], c[1])

    value = 0
    times = 0

    for _ in range(revolutions):
        if abs(value) >= 2:
            return times
        value = value*value + c
        times += 1
    return times

def make_coordinates(coordinates):
    new_x = coordinates[0]-HEIGHT/2
    new_x = new_x * ZOOM
    new_y = coordinates[1]-HEIGHT/2
    new_y = new_y * ZOOM
    return (new_x, new_y)

def graph():
    for x in range(HEIGHT):
        for y in range(WIDTH):
            coordinates = make_coordinates((x, y))
            mandelbrot_value = mandelbrot(coordinates, REVOLUTIONS)
            if mandelbrot_value == REVOLUTIONS:
                img.put("#000000", (x, y))
            else:
                img.put("#FFFFFF", (x, y))

graph()

root.mainloop()