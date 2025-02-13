# simpson function implementation - Lokaghna
import numpy as np
def trapezoidal(x_vals: np.ndarray, func: np.ufunc):
    print("Hello")

# simpson function implementation - Lokaghna
def simpson(x_vals: np.ndarray, func: np.ufunc):
    a = x_vals[0]
    b = x_vals[-1]
    approx = ((b-a)/6)(func(a)+4*func((a+b)/2)+func(b))
    return approx


def left_endpoint(x_vals: np.ndarray, func: np.ufunc):
    dx: np.diff(x_vals)
    return np.sum(func(x_vals[:-1]*dx))