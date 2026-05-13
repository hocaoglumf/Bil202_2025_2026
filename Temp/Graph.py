import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

y1 = x
y2 = x**2
y3 = np.sin(x)

plt.plot(x, y1, label="y = x")
plt.plot(x, y2, label="y = x^2")
plt.plot(x, y3, label="y = sin(x)")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Multiple Functions on One Graph")

plt.legend()
plt.grid(True)

plt.show()