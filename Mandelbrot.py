#!/usr/bin/env Python3
from PIL import Image,ImageDraw
from random import randrange
from time import time
    

def mandelbrot(x,y):
    a = 0
    b = 0
    img = Image.new("RGB",(x, y), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    for i in range(y):
        for j in range(x):
            Ci = ((i*2.4)/y)-1.2
            Cr = ((j*2.7)/x)-2.1
            Zi = 0
            Zr = 0
            for n in range(355):
                ZR = Zr
                Zr = Zr**2 - Zi**2 + Cr
                Zi = 2 * ZR * Zi + Ci
                if Zr**2 + Zi**2 >= 4:
                    break
            if Zr**2 + Zi**2 >= 4:
                draw.point((j,i),fill=(0,0,n))
            else:
                draw.point((j,i),fill=(0,0,0))
    img.show()
    img.save("/home/mahtar_nola/Bureau/Programation/test.png", "PNG")
