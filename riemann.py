# simpson function implementation - Lokaghna
import numpy as np
def trapezoidal(x_vals: np.ndarray, func: np.ufunc):
    print("Hello")

def simpson(x_vals: np.ndarray, func: np.ufunc):
    print("Hello")

def left_endpoint(x_vals: np.ndarray, func: np.ufunc):
    dx: np.diff(x_vals)
    return np.sum(func(x_vals[:-1]*dx))