import numpy as np
def get_points(vector,point):
    x_v, y_v, z_v = vector[0], vector[1], vector[2]
    x,y,z = point[0], point[1], point[2]

    x_res= x_v
    y_res= (y_v*(x_v-x)/x_v)+y
    z_res= (z_v*(x_v-x)/x_v)+z
    return (x_res, y_res, z_res)
    