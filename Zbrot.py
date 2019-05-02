#!/usr/bin/Python3.5
# -*- coding: utf-8 -*-

from Mandelbrot import *
from numpy import pi, sin
x = 901;
y = 1801;
n = 180;

for i in range(n,-1,-1):
	title = "./Images/Image%03d.png" % (i);
	coef = sin((i/n)*pi/2)
	Xmax = 1-(1.7375*coef);
	Xmin = -2+(1.2375*coef);
	Ymax = 3-(2.9*coef);
	Ymin = -3+(3.05*coef);
	nmax = 200+i;
	mandelbrot( x, y, title, Xmax, Xmin, Ymax, Ymin, nmax);
