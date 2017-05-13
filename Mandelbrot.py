#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from PIL import Image,ImageDraw
from math import sqrt

def mandelbrot(x,y):
    """int*int -> Nonetype
    Hypothèse: x > 0 and y > 0
    retourne la fractale de mandelbrot"""
    a = 0
    b = 0
    img = Image.new("RGB",(x, y), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    for i in range(y):
        for j in range(x):
            draw.point((j,i),fill=(0,0,point(x,y,i,j)))
    img.show()
    img.save("/home/mahtar_nola/Bureau/Programation/test.png", "PNG")

def point( x, y, i, j, Xmax = 1, Xmin = -2, Ymax = 1, Ymin = -1):
    """int^4 * float^4 -> int
    Hypoyhèse: min([x,y,i,j]) >= 0 and Xmin < Xmax and Ymin < Ymax
    retourne le nombre d'itération avant que la suite Zn diverge vers l'infini"""
    Ci = ((i*(Ymax-Ymin))/y)+Ymin
    Cr = ((j*(Xmax-Xmin))/x)+Xmin
    Zi = 0
    Zr = 0
    if ((Cr+1)**2)+(Ci**2) < 1/16:
        return(0)
    p = sqrt(((Cr-(1/4))**2)+(Ci**2))
    if Cr < p-(2*(p**2))+(1/4):
        return(0)
    for n in range(256):
        ZR = Zr
        Zr = Zr**2 - Zi**2 + Cr
        Zi = 2 * ZR * Zi + Ci
        if Zr**2 + Zi**2 >= 4:
            return(n)
    return(0)
