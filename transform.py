from matrix import *
from math import cos,sin,radians

def translate(matrix,args):
    x = args[0]
    y = args[1]
    z = args[2]
    m = new_matrix()
    ident(m)
    m[3][0] = x
    m[3][1] = y
    m[3][2] = z
    matrix_mult(matrix,m)
    replace(matrix,m)

def dilate(matrix,args):
    x = args[0]
    y = args[1]
    z = args[2]
    m = new_matrix()
    ident(m)
    m[0][0] = x
    m[1][1] = y
    m[2][2] = z
    matrix_mult(matrix,m)
    replace(matrix,m)

def rotate(matrix,args):
    axis = args[0]
#    print args[1]
    angle = float(radians(float(args[1])))
    ax = {
        'x': rotateX,
        'y': rotateY,
        'z': rotateZ
    }
    ax[axis](matrix,angle)

def rotateZ(matrix,angle):
    m = new_matrix()
    ident(m)
    m[0][0] = cos(angle)
    m[0][1] = sin(angle)
    m[1][0] = -1 * m[0][1]
    m[1][1] = m[0][0]
    matrix_mult(matrix,m)
    replace(matrix,m)

def rotateX(matrix,angle):
    m = new_matrix()
    ident(m)
    m[1][1] = cos(angle)
    m[1][2] = sin(angle)
    m[2][1] = -1 * m[1][2]
    m[2][2] = m[1][1]
    matrix_mult(matrix,m)
    replace(matrix,m)

def rotateY(matrix,angle):
    m = new_matrix()
    ident(m)
    m[2][2] = cos(angle)
    m[2][0] = sin(angle)
    m[0][2] = -1 * m[2][0]
    m[0][0] = m[2][2]
    matrix_mult(matrix,m)
    replace(matrix,m)
