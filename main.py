from display import *
from draw import *
from matrix import *
from parse import *
from transform import *
from math import cos,sin,tan,radians

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()
ident(transform)
csystems = [transform]
zbuf = new_zbuffer()

parse("bript",edges,polygons,csystems,screen,zbuf,color)
