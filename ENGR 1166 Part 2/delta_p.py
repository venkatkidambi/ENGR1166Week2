# imports
import math
from scipy import optimize

# function definition 
def k(x):
    return x - ((x ** 2) / 4) - ((math.log(x)) / 2) - (3 / 4)

def delta_p(xyz):
    alpha, A, t = xyz
    return 500040 * (alpha / (1 - alpha)) * (t / (A * k(alpha)))

# constrained optimization
bnds = ((0.01, 0.3), (0.0001, 0.092903), (0.0127, 0.3048))
p = optimize.minimize(delta_p, (0.1, 0.5, 0.75), bounds = bnds)

# output
print(f"delta_p: {p.fun}")
labels = ["alpha", "A", "t"]
for i in range(len(p.x)):
    print(f"{labels[i]}: {p.x[i]}")