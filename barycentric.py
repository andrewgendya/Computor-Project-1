# get_baryenctric_coordinates implementation - Andrew
import numpy as np


def get_barycentric_coordinates(triangle_coordinates, point_coordinates):
    x1,x2,x3=triangle_coordinates[0]
    y1,y2,y3=triangle_coordinates[1]
    x,y=point_coordinates
    denominator=(x2-x1)*(y2-y1)-(y3-y1)*(y2-y1)
    run1=((x2-x)*(y3-y)-(x3-x)*(y2-y))/denominator
    run2=((x3-x)*(y1-y)-(x1-x)*(y3-y))/denominator
    run3=1-run1-run2
    return np.array([run1,run2,run3])
# get_Caretsian_coordinates implementation - Devadarshini
def get_cartesian_coordinates:

# is_inside_triangle implementation - Lokaghna
def is_inside_triangle:
    return