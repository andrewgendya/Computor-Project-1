import numpy as np

# get_baryenctric_coordinates implementation - Andrew
def get_barycentric_coordinates(triangle_coordinates, point_coordinates):
    x1,x2,x3=triangle_coordinates[0]
    y1,y2,y3=triangle_coordinates[1]
    x,y=point_coordinates
    denominator=(x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    run1=((x2-x)*(y3-y)-(x3-x)*(y2-y))/denominator
    run2=((x3-x)*(y1-y)-(x1-x)*(y3-y))/denominator
    run3=1-run1-run2
    return np.array([run1,run2,run3])

# get_Caretsian_coordinates implementation - Devadarshini
# indent error because of space before function def below
def get_cartesian_coordinates(triangle_coordinates, barycentric_coordinates):
    #triangle_coordinates[0] = ("x1", "x2", "x3")
    #triangle_coordinates[1] = ("y1", "y2", "y3")
    #triangle_coordinates = np.array(triangle_coordinates)
    #barycentric_coordinates = 1, 2, 3
    #barycentric_coordinates = np.array(barycentric_coordinates)
    return np.dot(triangle_coordinates, barycentric_coordinates)

# is_inside_triangle implementation - Lokaghna
def is_inside_triangle(triangle_coordinates, point_coordinates):
    bary_coord = get_barycentric_coordinates(triangle_coordinates, point_coordinates)
    cartesian_point = get_cartesian_coordinates(triangle_coordinates, bary_coord)
    diff = np.abs(point_coordinates - cartesian_point)
    return np.all(bary_coord >= -1e-10) and np.all(diff < 0.01)
