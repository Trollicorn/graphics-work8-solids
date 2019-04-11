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
#zbuf = new_matrix(500,500,float("-inf"))

parse("script2",edges,polygons,csystems,screen,color)
