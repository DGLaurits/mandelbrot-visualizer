from PIL import Image
from numba import njit
import numpy as np

@njit
def make_coordinates(width, height, zoom, xy, offset_xy):
    new_x = np.array(xy[0]-width/2)
    new_x = new_x * zoom + offset_xy[0]
    new_y = np.array(xy[1]-height/2)
    new_y = new_y * zoom + offset_xy[1]
    return complex(new_x, new_y)

@njit()
def get_mandelbrot(size: tuple[int, int], revolutions: int, zoom: float, offset_xy: tuple[int, int]):
    coordinates = np.zeros(shape=(size[0], size[1]), dtype=np.complex128)

    for i, row in enumerate(coordinates):
        for j, c in enumerate(row):
            coordinates[i][j] = make_coordinates(size[0], size[1], zoom, (i, j), offset_xy)
        
    values = np.zeros(shape=coordinates.shape, dtype=coordinates.dtype)
    mandelbrot_revolutions = np.zeros(shape=coordinates.shape, dtype=np.int64)
    
    for _ in range(revolutions):
        values = values*values + coordinates
        mandelbrot_revolutions = np.where(np.abs(values) < 2, mandelbrot_revolutions+1, mandelbrot_revolutions)
    return mandelbrot_revolutions

def create_mandelbrot_image(size: tuple[int, int], revolutions: int, zoom: float, offset_xy: tuple[int, int]):
    color_factor = 255//revolutions
    img = Image.new("RGB", (size[0], size[1]))
    mandelbrot = get_mandelbrot(size, revolutions, zoom, offset_xy)
    for x in range(size[0]):
        for y in range(size[1]):
            img.putpixel((x, y), (color_factor*mandelbrot[x][y], color_factor*mandelbrot[x][y], color_factor*mandelbrot[x][y]))
    return img

