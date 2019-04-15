from display import *
from draw import *
from matrix import *
from parse import *
from transform import *
from math import cos,sin,tan,radians

screen = new_screen()
colors = [[255,0,0],[122,12,43],[45,56,124],[255,255,0],[0,255,0],[0,255,255],[0,0,255],[255,0,255]]
edges = []
polygons = []
transform = new_matrix()
ident(transform)
csystems = [transform]
zbuf = new_zbuffer()

parse("laser",edges,polygons,csystems,screen,zbuf,colors)
