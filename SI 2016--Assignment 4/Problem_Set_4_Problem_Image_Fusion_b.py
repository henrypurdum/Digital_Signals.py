#imports
import numpy as np
from scipy.misc import imread
import scipy.sparse as sparse
import scipy.sparse.linalg as linalg
import matplotlib.pyplot as plt

#read images
color = imread('vis.jpg')
ir = imread('ir.jpg', "True")
#ravel ir image
ir_ravel = ir.ravel(order='F')

#seperate then ravel color channels
R = color[:, :, 0]
G = color[:, :, 1]
B = color[:, :, 2]
R = R.ravel(order='F')
G = G.ravel(order='F')
B = B.ravel(order='F')

#put all raveled color channels together into one single array
y = np.concatenate((R, G, B, ir_ravel))

#build block matrix 'A'; first three rows then add fourth row
topOfA = sparse.identity(3*ir_ravel.size)
smallI = sparse.identity(ir_ravel.size)
#multiply matrix i by scalars to form fourth row
i1 = np.multiply(0.3, smallI)
i2 = np.multiply(0.6, smallI)
i3 = np.multiply(0.1, smallI)
#concatenate/stack fourth row
bottomOfA = sparse.hstack((i1, i2, i3))
#concatenate/stack all the rows
A = sparse.vstack((topOfA, bottomOfA))

#x = fused matrix (first product of least squares)
x = linalg.lsqr(A, y)[0] #pull first product
x = x.reshape([3, 760**2]) #reshape x to be a 2-dimensional array
x = np.around(x) #drop decimals to eliminate some noise
x_color = np.ndarray(color.shape) #define new array to use in elimination of 'blush'
#eliminate 'blush' from image by restricting pixel range
for i in range(0, 3):
    x[i, :] = np.maximum(np.minimum(x[i, :], 255), 0)
    x_color[:, :, i] = np.reshape(x[i, :], ir.shape, order='F')
x_color = np.multiply(x_color, -1) #invert colors of the image to put the colors back to normal
plt.imshow(x_color) #put image on the graph
plt.show() #shows graph
