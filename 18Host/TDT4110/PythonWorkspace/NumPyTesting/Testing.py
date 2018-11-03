import numpy as np
import matplotlib.pyplot as plt



x = np.arange(- np.pi, np.pi, 0.01)

y = np.sin(x)

plt.plot(x, y)
plt.axis([-np.pi, np.pi, -1.5, 1.5])

plt.show()
