import numpy as np
# left_endpoint - Andrew Gendy
def left_endpoint(x_vals: np.ndarray, func: np.ufunc):
    dx = np.diff(x_vals)
    # changed dx: to dx =
    return np.sum(func(x_vals[:-1])*dx)
    # moved "*dx" outside func call

# simpson function implementation - Devadarshini
def trapezoid(x_vals: np.ndarray, func: np.ufunc)->float:
    integral = np.diff(x_vals)
    return np.sum(((func(x_vals[:-1]))+(func(x_vals[1:])))/2*integral)


# simpson function implementation - Lokaghna Velugu Boreddi
def simpson(x_vals: np.ndarray, func: np.ufunc):
    a = x_vals[0]
    b = x_vals[-1]

    approx = ((b-a)/6)*(func(a)+4*func((a+b)/2)+func(b))
    return approx