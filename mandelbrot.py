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

def make_coordinates(width, height, zoom, xy):
    new_x = xy[0]-width/2
    new_x = new_x * zoom
    new_y = xy[1]-height/2
    new_y = new_y * zoom
    return (new_x, new_y)

def create_mandelbrot(size: tuple[int, int], revolutions: int, zoom: float):
    img = Image.new("RGB", (size[0], size[1]))
    for x in range(size[0]):
        for y in range(size[1]):
            coordinates = make_coordinates(size[0], size[1], zoom, (x, y))
            mandelbrot_value = mandelbrot(coordinates, revolutions)
            if mandelbrot_value == revolutions:
                img.putpixel((x, y), (200, 230, 255))
            else:
                img.putpixel((x, y), (0, 0, 0)) 
    return img