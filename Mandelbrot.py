# -*- coding: utf-8 -*-

from PIL import Image,ImageDraw
from math import sqrt

def mandelbrot(x,y, title = "./test.png", Xmax = 1, Xmin = -2, Ymax = 1, Ymin = -1, nmax = 300):
    """int*int -> Nonetype
    Hypothèse: x > 0 and y > 0
    retourne la fractale de mandelbrot"""
    a = 0
    img = Image.new("RGB",(x, y), "#FFFFFF")
    draw = ImageDraw.Draw(img)
    Y = range(y)
    X = range(x)
    for i in Y:
        for j in X:
            a = point(x, y, i, j, Xmax, Xmin, Ymax, Ymin, nmax)
            draw.point((j,i),fill=(255//23*(a%23),255//7*(a%7),255//17*(a%17)))
    #img.show()
    img.save(title, "PNG")

def point( x, y, i, j, Xmax, Xmin, Ymax, Ymin, nmax = 300):
    """int^4 * float^4 -> int
    Hypoyhèse: min([x,y,i,j]) >= 0 and Xmin < Xmax and Ymin < Ymax
    retourne le nombre d'itération avant que la suite Zn diverge vers l'infini"""
    Ci = ((i*(Ymin-Ymax))/y)+Ymax
    Cr = ((j*(Xmax-Xmin))/x)+Xmin
    Zi = 0
    Zr = 0
    if ((Cr+1)*(Cr+1))+(Ci*Ci) < 1/16:
        return(0)
    p = sqrt(((Cr-(1/4))*(Cr-(1/4)))+(Ci*Ci))
    if Cr < p-(2*(p*p))+(1/4):
        return(0)
    N = range(nmax)
    for n in N:
        ZR = Zr
        Zr = Zr*Zr - Zi*Zi + Cr
        Zi = 2 * ZR * Zi + Ci
        if Zr*Zr + Zi*Zi >= 4:
            return(n)
    return(0)
