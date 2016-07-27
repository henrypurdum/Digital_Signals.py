import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread

newArray = np.ndarray([1080, 1920, 50])

for i in range(50, 100, 1):
    img = imread('image_0' + str(i)+ '.jpg', "True")
    newArray[:, :, i - 50] = img
averageArray = np.median(newArray[:, :, :], axis=2)
imgplot = plt.imshow(averageArray)
imgplot.set_cmap('gray')
plt.show()
