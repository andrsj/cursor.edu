import scipy.signal 
import numpy as np 
import matplotlib.pyplot as plt


img = plt.imread('photo2.jpg')

# t = 1 - np.abs(np.linspace(-1, 1, 21))
# kernel = t.reshape(21, 1) * t.reshape(1, 21) 
# kernel /= kernel.sum()  # kernel should sum to 1! :) 
#                         # convolve 2d the kernel with each channel 
k = np.array(
    [
        [ 0  , 0  ,-0.5, 0  , 0  ],
        [ 0  , 1  , 1.5, 1  , 0  ],
        [-0.5, 1.5, 2  , 1.5,-0.5],
        [ 0  , 1  , 1.5, 1  , 0  ],
        [ 0  , 0  ,-0.5, 0  , 0  ]
    ],
    dtype=np.float64
)
k /= 10

r = scipy.signal.convolve2d(img[:,:,0], k, mode='full', boundary='fill', fillvalue=0) #, mode='same') 
g = scipy.signal.convolve2d(img[:,:,1], k, mode='full', boundary='fill', fillvalue=0) #, mode='same') 
b = scipy.signal.convolve2d(img[:,:,2], k, mode='full', boundary='fill', fillvalue=0) #, mode='same') 

# stack the channels back into a 8-bit colour depth image and plot it 
im_out = np.dstack([r, g, b]) 
im_out = (im_out).astype(np.uint8) 

print(im_out[0])

plt.subplot(1,2,1) 
plt.imshow(img) 
plt.subplot(1,2,2) 
plt.imshow(im_out) 

plt.show() 