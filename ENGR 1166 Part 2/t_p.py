import data
import constants
import matplotlib.pyplot as plt 

plt.plot(data.z, [data.delta_p(constants.alpha, constants.A, a) for a in data.z], label = "t vs. delta_p")
plt.plot(data.z, [1000 for a in data.z], label = "1000 Pa cutoff")
plt.xlabel("t (m)")
plt.ylabel("delta_p")
plt.title("t vs. delta_p")
plt.grid()
plt.legend()
plt.show()