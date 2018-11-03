import numpy as np
import matplotlib.pyplot as plt
import matplotlib2tikz.save as tikz_save


def integral(y, x):
    print(type(y))
    dx = x[1] - x[0]
    acc = 0
    for i in range(len(x)):
        acc += y(x[i]) * dx
    return acc


def four(x, y, n):
    a = x[0]
    b = x[len(x) - 1]
    l = (b - a) / 2
    ret = 1 / (2 * l) * integral(y, x)
    for i in range(1, n + 1):
        ret += np.cos(i * x) * (1 / l) * integral(y(x) * np.vectorize(np.cos)(i * x), x)
        ret += np.sin(i * x) * (1 / l) * integral(y(x) * np.vectorize(np.sin)(i * x), x)
    return ret


def test(y, x):
    return y * x


def f(x):
    return -1 if x < 0 else 1


x = np.arange(-np.pi, np.pi, 0.01)

y = np.vectorize(f)

i = 5

# print(integral(y(x) * np.vectorize(np.sin)(i * x), x))

plt.plot(x, y(x), 'black')
plt.plot(x, four(x, y, 3))
plt.axis([-4, 4, -1.5, 1.5])
plt.grid(True)
# plt.box(False)
plt.savefig("plot.png")

# tikz_save("plot.tikz", figureheight='\\figureheight', figurewidth='\\figurewidth')
