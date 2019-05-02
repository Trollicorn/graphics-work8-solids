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
    corners.sort(key=lambda x:x[1])
#    top = max(corners,key=lambda x: x[1])
#    bot = min(corners,key=lambda x: x[1])
#    corners.remove(top)
#    corners.remove(bot)
#    mid = corners.pop(0)
    bot = corners[0]
    mid = corners[1]
    top = corners[2]
    Bx = x0 = x1 = bot[0]
    Bz = z0 = z1 = bot[2]
    By = int(bot[1])

    Tx = top[0]
    Tz = top[2]
    Ty = int(top[1])
    Mx = mid[0]
    Mz = mid[2]
    My = int(mid[1])
    BtoT = Ty - By * 1.0 + 1
    BtoM = My - By * 1.0 + 1
    MtoT = Ty - My * 1.0 + 1
    switch = False
    dx0 = (Tx-Bx)/BtoT if BtoT != 0 else 0
    dz0 = (Tz-Bz)/BtoT if BtoT != 0 else 0
    dx1 = (Mx-Bx)/BtoM if BtoM != 0 else 0
    dz1 = (Mz-Bz)/BtoM if BtoM != 0 else 0
    for y in range (By,Ty+1):
        if not switch and y >= My:
            dx1 = (Tx-Mx)/MtoT if MtoT != 0 else 0
            dz1 = (Tz-Mz)/MtoT if MtoT != 0 else 0
            x1 = Mx
            z1 = Mz
            switch = True
        draw_line(int(x0),y,z0,int(x1),y,z1,screen,zbuffer,color)
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
    if ( abs(x1-x0) >= abs(y1 - y0) ): #octants 1/8
        wide = True
        loop_start = x
        loop_end = x1
        dx_east = dx_northeast = 1
        dy_east = 0
        d_east = A
        distance = x1 - x + 1
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
        distance = abs(y1 - y) + 1
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
    dz = (z1 - z0) / distance if distance != 0 else 0
    while ( loop_start < loop_end ):
        plot( screen, zbuffer, color, x, y, z )
        if ( (wide and ((A > 0 and d > 0) or (A < 0 and d < 0))) or
             (tall and ((A > 0 and d < 0) or (A < 0 and d > 0 )))):
            x+= dx_northeast
            y+= dy_northeast
            d+= d_northeast
        else:
            x+= dx_east
            y+= dy_east
            d+= d_east
        z+= dz
        loop_start+= 1
    plot( screen, zbuffer, color, x, y, z )
