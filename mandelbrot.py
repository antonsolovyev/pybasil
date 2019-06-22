#!/usr/bin/env python

import numpy
import math
from PIL import Image, ImageDraw


# Mandelbrot max iterations
MAX_ITERATIONS = 100
# Grid points per unit interval
RESOLUTION = 300
# Bounding box
MIN_X = -2.5
MAX_X = 1.0
MIN_Y = -1.5
MAX_Y = 1.5

width = int(RESOLUTION * (MAX_X - MIN_X))
height = int(RESOLUTION * (MAX_Y - MIN_Y))
step = 1.0 / RESOLUTION


def get_color_rgb(i, z):
    if i == MAX_ITERATIONS:
        return (255, 255, 255)

    return (0, 0, 0)


def get_color_hsv(i, z):
    if i == MAX_ITERATIONS:
        return (0, 0, 0)

    hue = i + 1.0 - math.log(math.log2(abs(z)))
    hue = hue / MAX_ITERATIONS

    return (int(hue * 255), 255, 255)


def draw(image, c, i, z):
    # Move origin and scale
    c = (c - complex(MIN_X, MIN_Y)) / step

    # Draw
    color = get_color_hsv(i, z)
    image.point([c.real, c.imag], color)


def main():
    print('Building...')

    image = Image.new('HSV', (width, height), (0, 0, 0))
    # image = Image.new('RGB', (width, height), (0, 0, 0))
    image_draw = ImageDraw.Draw(image)

    for x in numpy.arange(MIN_X, MAX_X, step):
        for y in numpy.arange(MIN_Y, MAX_Y, step):
            c = complex(x, y)
            z = complex(0, 0)

            i = 0
            while i < MAX_ITERATIONS:
                i += 1
                z = z * z + c
                if abs(z) > 2:
                    break

            draw(image_draw, c, i, z)

    image.show()
    image.close()

    print('Done.')

if __name__ == '__main__':
    main()
