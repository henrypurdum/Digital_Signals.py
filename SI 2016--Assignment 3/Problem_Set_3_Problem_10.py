import numpy as np
from scipy import misc
import scipy
from matplotlib import pyplot as plt
import matplotlib

def decryptMessage(imgin):
    img = misc.imread(imgin, True)
    img = np.array(img)

    A = np.ndarray(img.shape)
    A[:] = img[:] % 2
    A = A.reshape(img.size, order = 'f')
    A = np.around(A)
    out = ""
    for i in A:
        if i == 0:
            out += "0"
        else:
            out += "1"
    print out


def encryptMessage(message, image, save):
    imA = misc.imread(image, True)
    A = np.array(imA)
    X = A.shape
    A = A.reshape(A.size, order = 'f')
    message = np.lib.pad(message, (0, (A.size-message.size)), 'constant', constant_values = (0))
    A[:] = A[:] - A[:] % 2
    A[:] = A[:] + message[:]
    out = A.reshape(X, order = 'f')
    new = np.ndarray([out.shape[0], out.shape[1], 3])
    new[:, :, 0] = out[:, :]
    new[:, :, 1] = out[:, :]
    new[:, :, 2] = out[:, :]
    matplotlib.image.imsave(save, new)
    return save
b = np.array([0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,0,1,1,0,0,1,0,1,0,1,1,0,0,0,1,1,0,1,1,1,0,0,1,0,0,1,1,0,0,1,0,1,0,1,1,1,0,1,0,0])
x = decryptMessage(encryptMessage(b, "fb.png", "topsecret.png"))
