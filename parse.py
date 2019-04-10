from transform import *
from matrix import *
from draw import *
from curve import *
from solid import *

def argify(line):
    args = line.split()
    for i in range(len(args)):
        try:
            args[i] = float(args[i])
        except ValueError:
    #        print(args[0])
            pass
    return args

def parse(fname, edge, polygon, csystems, screen, color):
    transform = {
        "scale": dilate,
        "move": translate,
        "rotate": rotate
    }
    shape = {
        "line": add_edge,
        "circle": circle,
        "hermite": hermite,
        "bezier": bezier
    }
    solid = {
        "box": box,
        "sphere": sphere,
        "torus": torus
    }
    f = open(fname, 'r')

    for line in f:
    #    print(type(line))
        line = line[:len(line)-1]
        if line in transform:
            #print("[" + line + "]")
            #print_matrix(csystems[-1])
            args = f.next()
            #print(args)
            args = argify(args)
            transform[line](csystems[-1],args)

        elif line in shape:
            args = f.next()
            args = argify(args)
            shape[line](edge,args)
            matrix_mult(csystems[-1],edge)
            draw_lines(edge,screen,color)
            edge = []
        elif line in solid:
            args = f.next()
            args = argify(args)
            solid[line](polygon,args)
            matrix_mult(csystems[-1],polygon)
            draw_polygons(polygon,screen,color)
            polygon = []
        #elif line == "apply":
        #    matrix_mult(orders,edge)
        #    matrix_mult(orders,polygon)
        #    clear_screen(screen)
        #    draw_lines(edge,screen,color)
        #    draw_polygons(polygon,screen,color)
        #elif line == "ident":
        #    orders = new_matrix()
        #    ident(orders)
        elif line == "push":
            csystems.append(duplicate(csystems[-1]))
        elif line == "pop":
            del csystems[-1]

        elif line == "save":
    #        print_matrix(edge)
            name = f.next()
            name = name[:len(name)-1]
            save_extension(screen,name)
        elif line == "display":
    #        clear_screen(screen)
    #        draw_lines(edge,screen,color)
    #        draw_polygons(polygon,screen,color)
#            print_matrix(edge)
            display(screen)
        #elif line == "clear":
        #    edge = []
        #    polygon = []
    #    else:
    #        print line
    f.close()
