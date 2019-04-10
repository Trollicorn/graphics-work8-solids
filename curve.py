from matrix import *
from draw import *
from math import cos,sin,pi

def circle(edge, args): #[cx,cy,cz,r]
    cx = args[0]
    cy = args[1]
    cz = args[2]
    r = args[3]
    num = 100.0
    for t in range(int(num)):
        tr = t/num
        x0 = int(r*cos(2*pi*tr)+cx)
        y0 = int(r*sin(2*pi*tr)+cy)
        x1 = int(r*cos(2*pi*(tr+1.0/num))+cx)
        y1 = int(r*sin(2*pi*(tr+1.0/num))+cy)
        stuff = [x0,y0,cz,x1,y1,cz]
        add_edge(edge,stuff)

def bezier(edge, args): #[x0,y0,x1,y1,x2,y2,x3,y3]
    x0 = args[0]
    y0 = args[1]
    x1 = args[2]
    y1 = args[3]
    x2 = args[4]
    y2 = args[5]
    x3 = args[6]
    y3 = args[7]
    b = [[-1,3,-3,1],[3,-6,3,0],[-3,3,0,0],[1,0,0,0]]
    #|-1  3 -3  1|
    #| 3 -6  3  0|
    #|-3  3  0  0|
    #| 1  0  0  0|
    g = [[x0,x1,x2,x3],[y0,y1,y2,y3]]
    matrix_mult(b,g)
    # now g = [[ax,bx,cx,dx],[ay,by,cy,dy]]
    funx = lambda t: int(g[0][0]*t*t*t + g[0][1]*t*t + g[0][2]*t + g[0][3])
    funy = lambda t: int(g[1][0]*t*t*t + g[1][1]*t*t + g[1][2]*t + g[1][3])
    num = 100.0
    for t in range(int(num)):
        tr = t/num
        lx0 = funx(tr)
        ly0 = funy(tr)
        lx1 = funx(tr+1.0/num)
        ly1 = funy(tr+1.0/num)
        stuff = [lx0,ly0,0,lx1,ly1,0]
        add_edge(edge,stuff)

def hermite(edge, args): #[x0,y0,x1,y1,rx0,ry0,rx1,ry1]
    x0 = args[0]
    y0 = args[1]
    x1 = args[2]
    y1 = args[3]
    rx0 = args[4]
    ry0 = args[5]
    rx1 = args[6]
    ry1 = args[7]
    h = [[2,-3,0,1],[-2,3,0,0],[1,-2,1,0],[1,-1,0,0]]
    #| 2 -2  1  1|
    #|-3  3 -2 -1|
    #| 0  0  1  0|
    #| 1  0  0  0|
    g = [[x0,x1,rx0,rx1],[y0,y1,ry0,ry1]]
    matrix_mult(h,g)
    # now g = [[ax,bx,cx,dx],[ay,by,cy,dy]]
    funx = lambda t: int(g[0][0]*t*t*t + g[0][1]*t*t + g[0][2]*t + g[0][3])
    funy = lambda t: int(g[1][0]*t*t*t + g[1][1]*t*t + g[1][2]*t + g[1][3])
    num = 100.0
    for t in range(int(num)):
        tr = t/num
        lx0 = funx(tr)
        ly0 = funy(tr)
        lx1 = funx(tr+1.0/num)
        ly1 = funy(tr+1.0/num)
        stuff = [lx0,ly0,0,lx1,ly1,0]
        add_edge(edge,stuff)
