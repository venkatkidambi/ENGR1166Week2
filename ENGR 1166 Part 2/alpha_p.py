import data
import constants
import matplotlib.pyplot as plt 

plt.plot(data.x, [data.delta_p(a, constants.A, constants.t) for a in data.x], label = "alpha vs. delta_p")
plt.plot(data.x, [1000 for a in data.x], label = "1000 Pa cutoff")
plt.xlabel("alpha")
plt.ylabel("delta_p")
plt.title("alpha vs. delta_p")
plt.grid()
plt.legend()
plt.show()