#!/usr/bin/Python3.5
# -*- coding: utf-8 -*-

from tkinter import *
from Mandelbrot import point

fen = Tk()
l = fen.winfo_screenwidth()*7//10
h = fen.winfo_screenheight()*7//10
Abscisse = (fen.winfo_screenwidth()-l)//2
Ordonné = (fen.winfo_screenheight()-h)//2
fen.title("Mandelbrot")
fen.geometry("%dx%d%+d%+d" % (l,h,Abscisse,Ordonné))
canvas = Canvas(fen, width = l, height = h, bg = "#000000")
img = PhotoImage(width = l, height = h)
canvas.create_image((0, 0), image = img, state = "normal", anchor = NW)
global pady
global padx
padx = l/10
pady = h/10
global X
global Y
X = 0
Y = 0
global Ymax
global Xmax
global Ymin
global Xmin
global n 
n = 150
#Coucou !! "inconu?" 12/05/17 club d'échec UPMC
if l/h > 3/2:
    Marge = ((l*2/h)-3)/2
    Xmax = 1+Marge
    Xmin = -2-Marge
    Ymax = 1
    Ymin = -1
elif l/h < 3/2:
    Ymax = (3*h)/(2*l)
    Ymin = -Ymax
    Xmax = 1
    Xmin = -2


def mandelbrot(n):
    """None -> NoneType
    Hypoyhèse: ø
    Génère la fractale de mandelbrot"""
    for i in range(h):
        for j in range(l):
            b = point( l, h, i, j, Xmax, Xmin, Ymin, Ymax,n)
            img.put("#%02x%02x%02x" % (255//23*(b%23),255//7*(b%7),255//17*(b%17)),(j, i))
            
def Sourie(evt):
    """None -> NoneType
    Hypoyhèse: ø
    Déplace le rectangle en fonction de la position de la sourie"""
    global X
    global Y
    X = evt.x
    Y = evt.y
    rect()
    if X-padx < 0 or X+padx > l or Y-pady < 0 or Y+pady > h:
        canvas.coords(rectangle, 2*l, 2*h, 2*l, 2*h)
        
def rect():
    """None -> NoneType
    Hypoyhèse: ø
    Déplace le rectangle en fonction de la position de la sourie"""
    canvas.coords(rectangle, X-padx, Y-pady, X+padx, Y+pady)
    
def Zoom(evt):
    """None -> NoneType
    Hypoyhèse: ø
    Modifie la taille du rectangle et génère le zoom"""
    global pady
    global padx
    global Ymax
    global Xmax
    global Ymin
    global Xmin
    global n
    zoom = evt.num
    if 5 == zoom or zoom == 4:
        pady += (zoom-4.5)*h/100
        padx += (zoom-4.5)*l/100
        if pady <= 0 or padx <= 0:
            pady = h/1000
            padx = l/1000
        rect()
    if 1 == zoom:
        x = (Xmax-Xmin)
        y = (Ymax-Ymin)
        Xmax = ((X+padx)*x/l)+Xmin
        Xmin = ((X-padx)*x/l)+Xmin
        Ymax = ((Y+pady)*y/h)+Ymin
        Ymin = ((Y-pady)*y/h)+Ymin
        n *= 1.3
        print(n)
        print("x= ",(Xmax+Xmin)/2)
        print("y= ",(Ymax+Ymin)/2)
        print()
        mandelbrot(int(n))

mandelbrot(n)
rectangle = canvas.create_rectangle(l,l,l,l, outline = "white")
canvas.focus_set()
canvas.bind("<Motion>", Sourie)
canvas.bind("<Button>", Zoom)
canvas.pack()
mainloop()
