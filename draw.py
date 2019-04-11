from display import *
from matrix import *
import random

def draw_lines( matrix, screen, color ):
    for i in range(0,len(matrix)-1,2):
        #addition
        draw_line(matrix[i][0], matrix[i][1], matrix[i+1][0], matrix[i+1][1],screen,color)

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

def draw_polygons(polygons, screen, color):
    #print(polygons)
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
            scanline(polygons[i],polygons[i+1],polygons[i+2],screen,[random.randint(0,255),random.randint(0,255),random.randint(0,255)])
            draw_line(polygons[i][0], polygons[i][1], polygons[i+1][0], polygons[i+1][1],screen,[0,0,255])
            draw_line(polygons[i+1][0], polygons[i+1][1], polygons[i+2][0], polygons[i+2][1],screen,[0,0,255])
            draw_line(polygons[i+2][0], polygons[i+2][1], polygons[i][0], polygons[i][1],screen,[0,0,255])

def scanline(c0,c1,c2,screen,color):
    corners = [c0,c1,c2]
    top = max(corners,key=lambda x: x[1])
    bot = min(corners,key=lambda x: x[1])
    corners.remove(top)
    corners.remove(bot)
    mid = corners.pop(0)
    Bx = x0 = x1 = bot[0]
    By = int(bot[1])
    Tx = top[0]
    Ty = int(top[1])
    Mx = mid[0]
    My = int(mid[1])
    diff0 = (Tx-Bx)/(Ty-By)
    if My != By:
        diff1 = (Mx-Bx)/(My-By)
#        print "Mx-Bx"
    else:
        diff1 = (Tx-Mx)/(Ty-My)
        x1 = Mx
#        print "Tx-Mx"
#    print [Bx,By]
#    print [Mx,My]
#    print [Tx,Ty]
#    print diff0
#    print diff1
    for y in range (By,Ty):
        draw_line(x0,y,x1,y,screen,color)
        x0 += diff0
        x1 += diff1
        if y == My and Ty != My:
            diff1 = (Tx-Mx)/(Ty-My)

def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
