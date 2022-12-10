import numpy as np
import matplotlib.pyplot as plt
from function import *

def draw_line(vector, point1, vector2, point2):

    ax1 = plt.figure().add_subplot(projection='3d')

    #line1
    _point1 = get_points(vector, point1)
    x1, y1, z1 = point1[0], point1[1], point1[2]
    _x1, _y1, _z1 = _point1[0], _point1[1], _point1[2]

    #line2
    _point2 = get_points(vector2, point2)
    x2, y2, z2 = point2[0], point2[1], point2[2]
    _x2, _y2, _z2 = _point2[0], _point2[1], _point2[2]

    x, y, z = [x1, _x1], [y1, _y1], [z1, _z1]
    _x, _y, _z = [x2, _x2], [y2, _y2], [z2, _z2]

    ax1.scatter(x, y, z, s = 100)
    ax1.scatter(_x, _y, _z, s = 100)
    ax1.plot(x, y, z)
    ax1.plot(_x, _y, _z)
    plt.savefig('images/result.png', bbox_inches='tight')
