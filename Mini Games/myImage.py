import numpy as np

myImage = np.zeros([500, 500])
myImage[1:100, 1:200] = 255

import matplotlib.pyplot as plt
imgplot = plt.imshow(myImage)
plt.show()

















