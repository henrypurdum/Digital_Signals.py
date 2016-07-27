import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imread

newArray = np.ndarray([1080, 1920, 3, 50])
height = 1080
width = 1920

for i in range(50, 100, 1):
    img = imread("image_0" + str(i) + ".jpg")
    newArray[:, :, :, i - 50] = img

average1Array = np.median(newArray[:, :, 0, :], axis = 2)
average2Array = np.median(newArray[:, :, 1, :], axis = 2)
average3Array = np.median(newArray[:, :, 2, :], axis = 2)

avgArray = np.ndarray([height, width, 3])
avgArray[:, :, 0] = average1Array
avgArray[:, :, 1] = average2Array
avgArray[:, :, 2] = average3Array

newArray = newArray.astype(float)
avgArray = avgArray * -1
avgArray = np.around(avgArray)
imgplot = plt.imshow(avgArray)
plt.show()
