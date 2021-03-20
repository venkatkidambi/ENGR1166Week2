import data
import constants
import matplotlib.pyplot as plt 

plt.plot(data.y, [data.delta_p(constants.alpha, a, constants.t) for a in data.y], label = "A vs. delta_p")
plt.plot(data.y, [1000 for a in data.y], label = "1000 Pa cutoff")
plt.xlabel("A (m^2)")
plt.ylabel("delta_p")
plt.title("A vs. delta_p")
plt.grid()
plt.legend()
plt.show()