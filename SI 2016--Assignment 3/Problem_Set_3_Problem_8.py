import numpy as np
from matplotlib import pyplot as plt


def makePolyData():
  nPts = 1000
  x = np.linspace(0, 10, nPts)
  y = 0.4*np.ones(nPts) + 1.2*np.power(x, 2) + -0.1*np.power(x, 3) + 0.001*np.power(x, 4)
  y = y + 2*np.random.randn(y.size)
  return(x, y)

(x, y) = makePolyData()
plt.plot(x, y, '.')

A = [x**4, x**3, x**2, x, np.ones(x.shape)]

invA = np.linalg.pinv(A)
coef = np.matmul(y, invA)
print coef

nPts = 1000
x = np.linspace(0, 10, nPts)
y = coef[3] * np.ones(nPts) + coef[2] * np.power(x, 2) + coef[1] * np.power(x, 3) + coef[0] * np.power(x, 4)
plt.plot(x, y, '.')
plt.show()
