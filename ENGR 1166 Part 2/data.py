import math
import numpy as np

def k(x):
    return x - ((x ** 2) / 4) - ((math.log(x)) / 2) - (3 / 4)

def delta_p(alpha, A, t):
    return 500040 * (alpha / (1 - alpha)) * (t / (A * k(alpha)))

x = [i for i in np.arange(0.01, 0.05, 0.0001)]
y = [j for j in np.arange(0.01, 0.092903, 0.001)]
z = [k for k in np.arange(0.0127, 0.3048, 0.01)]