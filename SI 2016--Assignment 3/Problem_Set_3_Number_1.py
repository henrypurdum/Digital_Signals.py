import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img_1 = Image.open('photo.jpg')
img_2 = Image.open('tumblr_krezhwqcbK1qa13gio1_500.jpg')

alpha = np.linspace(0, 1, 6)

for i in range(0, 6):
    pic = (alpha[i] * img_1) + (img_2 * (1-alpha[i]))
    pic = np.around(pic)
    pic = np.multiply(pic, -1)
    imgplot = plt.imshow(pic)
    plt.show()
