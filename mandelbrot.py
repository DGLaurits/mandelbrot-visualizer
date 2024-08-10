from PIL import Image, ImageColor

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

def make_coordinates(width, height, zoom, xy, offset_xy):
    new_x = xy[0]-width/2
    new_x = new_x * zoom + offset_xy[0]
    new_y = xy[1]-height/2
    new_y = new_y * zoom + offset_xy[1]
    return (new_x, new_y)

def create_mandelbrot(size: tuple[int, int], revolutions: int, zoom: float, offset_xy: tuple[int, int]):
    color_factor = 255//revolutions
    img = Image.new("RGB", (size[0], size[1]))
    for x in range(size[0]):
        for y in range(size[1]):
            coordinates = make_coordinates(size[0], size[1], zoom, (x, y), offset_xy)
            mandelbrot_value = mandelbrot(coordinates, revolutions)
            img.putpixel((x, y), (color_factor*mandelbrot_value, color_factor*mandelbrot_value, color_factor*mandelbrot_value))
    return img