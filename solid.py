from matrix import *
from math import cos,sin,pi
from draw import *

def box(polygon, args): #[x,y,z,w,h,d]
    x = args[0]
    y = args[1]
    z = args[2]
    w = args[3] #width
    h = args[4] #height
    d = args[5] #depth
    ex = x + w
    ey = y - h
    ez = z - d
    #parallel xy plane
    add_poly(polygon,ex, y, z, x, y, z, x,ey, z)
    add_poly(polygon, x,ey, z,ex,ey, z,ex, y, z)
    add_poly(polygon, x, y,ez,ex, y,ez,ex,ey,ez)
    add_poly(polygon,ex,ey,ez, x,ey,ez, x, y,ez)
    #parallel yz plane
    add_poly(polygon, x, y,ez, x,ey,ez, x,ey, z)
    add_poly(polygon, x,ey, z, x, y, z, x, y,ez)
    add_poly(polygon,ex, y, z,ex,ey, z,ex,ey,ez)
    add_poly(polygon,ex,ey,ez,ex, y,ez,ex, y, z)
    #parallel xz plane
    add_poly(polygon, x, y,ez, x, y, z,ex, y, z)
    add_poly(polygon,ex, y, z,ex, y,ez, x, y,ez)
    add_poly(polygon, x,ey, z, x,ey,ez,ex,ey,ez)
    add_poly(polygon,ex,ey,ez,ex,ey, z, x,ey, z)

def sphere(polygon,args): #[x,y,z,r]
    x = args[0]
    y = args[1]
    z = args[2]
    r = args[3]
    n = 10
    p = p_sphere(x,y,z,r,n)
    for i in range(len(p)-1):
#        """
        a = i + 1
        b = (i+n)%(n*n)
        c = (i+n+1)%(n*n)
        if i % n == 0:
            add_poly(polygon,p[i][0],p[i][1],p[i][2],
                             p[a][0],p[a][1],p[a][2],
                             p[c][0],p[c][1],p[c][2])
        elif i % n == n-2:
            add_poly(polygon,p[i][0],p[i][1],p[i][2],
                             p[a][0],p[a][1],p[a][2],
                             p[b][0],p[b][1],p[b][2])
    #    elif i % n == n-1:
    #        pass
        else:
            add_poly(polygon,p[i][0],p[i][1],p[i][2],
                             p[a][0],p[a][1],p[a][2],
                             p[b][0],p[b][1],p[b][2])
            add_poly(polygon,p[a][0],p[a][1],p[a][2],
                             p[c][0],p[c][1],p[c][2],
                             p[b][0],p[b][1],p[b][2])
"""
    if i % n < n - 2:
        add_poly(polygon,p[(i+n)%(n*n)][0],p[(i+n)%(n*n)][1],p[(i+n)%(n*n)][2],
                         p[i+1][0],p[i+1][1],p[i+1][2],
                         p[(i+n+1)%(n*n)][0],p[(i+n+1)%(n*n)][1],p[(i+n+1)%(n*n)][2])
        add_poly(polygon,p[i+1][0],p[i+1][1],p[i+1][2],
                         p[i+2][0],p[i+2][1],p[i+2][2],
                         p[(i+n+1)%(n*n)][0],p[(i+n+1)%(n*n)][1],p[(i+n+1)%(n*n)][2])
"""

#    print(points)

def torus(polygon,args): #[x,y,z,r1,r2]
    x = args[0]
    y = args[1]
    z = args[2]
    r1 = args[3] #small circles
    r2 = args[4] #big circle
    n = 10
    p = p_torus(x,y,z,r1,r2,n)
#    print(p)
#    print(len(p))
    for i in range(len(p)):
        a = (i+1)%n+i//n*n
        b = (a + n) % (n*n) #((i+1)%n+i//n*n+n) %(n*n)
        c = (i+n)%(n*n)
        add_poly(polygon,p[i][0],p[i][1],p[i][2],
                         p[a][0],p[a][1],p[a][2],
                         p[c][0],p[c][1],p[c][2])
        add_poly(polygon,p[a][0],p[a][1],p[a][2],
                         p[b][0],p[b][1],p[b][2],
                         p[c][0],p[c][1],p[c][2])

def p_sphere(x,y,z,r,n):
    points = []
    num = float(n)
    for i in range(int(num)):
        phi = 2*pi*i/num
        cosphi = cos(phi)
        sinphi = sin(phi)
        for j in range(int(num)):
            theta = pi*j/(num-1)
            sintheta = sin(theta)
            costheta = cos(theta)
            points.append([int(r*costheta)+x, int(r*sintheta*cosphi)+y, int(r*sintheta*sinphi)+z])
    return points

def p_torus(x,y,z,r1,r2,n):
    points = []
    num = float(n)
    for i in range(int(num)):
        phi = 2*pi*i/num
        cosphi = cos(phi)
        sinphi = sin(phi)
        for j in range(int(num)):
            theta = 2*pi*j/num
            sintheta = sin(theta)
            costheta = cos(theta)
            points.append([int(cosphi*(r1*costheta+r2))+x, int(r1*sintheta)+y, int(sinphi*(r1*costheta+r2))+z])
    return points
