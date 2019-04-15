from display import *
from matrix import *
import random

def draw_lines( matrix, screen, zbuffer,color ):
    for i in range(0,len(matrix)-1,2):
        #addition
        draw_line(matrix[i][0],matrix[i][1],matrix[i][2],matrix[i+1][0],matrix[i+1][1],matrix[i+1][2],screen,zbuffer,color)

def add_edge( matrix, args): #[x0, y0, z0, x1, y1, z1]
#    print(args)
    add_point(matrix,args[0],args[1],args[2])
    add_point(matrix,args[3],args[4],args[5])

def add_point( matrix, x, y, z=0 ):
    matrix.append([x,y,z,1])

def add_poly(polygon,x0,y0,z0,x1,y1,z1,x2,y2,z2):
    add_point(polygon,x0,y0,z0)
    add_point(polygon,x1,y1,z1)
    add_point(polygon,x2,y2,z2)

def draw_polygons(polygons, screen, zbuffer,colors):
    #print(polygons)
#    clrs = len(colors)
#    c = 0
    for i in range(0,len(polygons)-1,3):
        norm = surf(polygons,i)
#        view = [0,0,1]
#        n = dot(norm,view) #cosine theta
#        theta = math.degrees(math.acos(n))
#        if math.fabs(theta) < 90:
        if norm[2] > 0:
        #    print polygons[i]
        #    print polygons[i+1]
        #    print polygons[i+2]
        #    print "good"
    #        color = colors[c%clrs]
    #        c += 1
            color = colors[0]
            colors.append(colors.pop(0))
            scanline(polygons[i],polygons[i+1],polygons[i+2],screen,zbuffer,color)
#            draw_line(polygons[i][0],polygons[i][1],polygons[i][2],polygons[i+1][0],polygons[i+1][1],polygons[i+1][2],screen,zbuffer,[255,255,255])
#            draw_line(polygons[i+1][0],polygons[i+1][1],polygons[i+1][2],polygons[i+2][0],polygons[i+2][1],polygons[i+2][2],screen,zbuffer,[255,255,255])
#            draw_line(polygons[i+2][0],polygons[i+2][1],polygons[i+2][2],polygons[i][0],polygons[i][1],polygons[i][2],screen,zbuffer,[255,255,255])

def scanline(c0,c1,c2,screen,zbuffer,color):
    corners = [c0,c1,c2]
    top = max(corners,key=lambda x: x[1])
    bot = min(corners,key=lambda x: x[1])
    corners.remove(top)
    corners.remove(bot)
    mid = corners.pop(0)
    Bx = x0 = x1 = bot[0]
    By = bot[1]
    Bz = z0 = z1 = bot[2]
    Tx = top[0]
    Ty = top[1]
    Tz = top[2]
    Mx = mid[0]
    My = mid[1]
    Mz = mid[2]
    switch = False
    if int(Ty) == int(By):
        dx0 = 0
        dz0 = 0
    else:
        dx0 = (Tx-Bx)/1.0/(int(Ty)-int(By))
        dz0 = (Tz-Bz)/1.0/(int(Ty)-int(By))
    if int(My) == int(By):
        dx1 = 0
        dz1 = 0
    else:
        dx1 = (Mx-Bx)/1.0/(int(My)-int(By))
        dz1 = (Mz-Bz)/1.0/(int(My)-int(By))
#        print "Tx-Mx"
#    print [Bx,By]
#    print [Mx,My]
#    print [Tx,Ty]
#    print d0
#    print d1
#    y = By
#    while y < Ty + 1:
    for y in range (int(By),int(Ty)):
        if not switch and y >= int(My):
            if int(Ty)== int(My):
                dx1 = 0
                dz1 = 0
            else:
                dx1 = (Tx-Mx)/1.0/(int(Ty)-int(My))
                dz1 = (Tz-Mz)/1.0/(int(Ty)-int(My))
            x1 = Mx
            z1 = Mz
            switch = True
        draw_line(x0,y,z0,x1,y,z1,screen,zbuffer,color)
        x0 += dx0
        z0 += dz0
        x1 += dx1
        z1 += dz1


def draw_line( x0, y0, z0, x1, y1, z1, screen, zbuffer, color ):
    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        zt = z0
        x0 = x1
        y0 = y1
        z0 = z1
        x1 = xt
        y1 = yt
        z1 = zt
    x = x0
    y = y0
    z = z0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)
    wide = False
    tall = False
    dz = (z1-z0)/(x1-x0+1)
    if ( abs(x1-x0) >= abs(y1 - y0) ): #octants 1/8
        wide = True
        loop_start = x
        loop_end = x1
        dx_east = dx_northeast = 1
        dy_east = 0
        d_east = A
        if ( A > 0 ): #octant 1
            d = A + B/2
            dy_northeast = 1
            d_northeast = A + B
        else: #octant 8
            d = A - B/2
            dy_northeast = -1
            d_northeast = A - B
    else: #octants 2/7
        tall = True
        dx_east = 0
        dx_northeast = 1
        if ( A > 0 ): #octant 2
            d = A/2 + B
            dy_east = dy_northeast = 1
            d_northeast = A + B
            d_east = B
            loop_start = y
            loop_end = y1
        else: #octant 7
            d = A/2 - B
            dy_east = dy_northeast = -1
            d_northeast = A - B
            d_east = -1 * B
            loop_start = y1
            loop_end = y
    while ( loop_start < loop_end ):
        plot( screen, zbuffer, color, x, y, z )
        z += dz
        if ( (wide and ((A > 0 and d > 0) or (A < 0 and d < 0))) or
             (tall and ((A > 0 and d < 0) or (A < 0 and d > 0 )))):
            x+= dx_northeast
            y+= dy_northeast
            d+= d_northeast
        else:
            x+= dx_east
            y+= dy_east
            d+= d_east
        loop_start+= 1
    plot( screen, zbuffer, color, x, y, z )
