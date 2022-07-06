import time

import numpy as np
import glob
from PIL import Image
import matplotlib.pyplot as plt


pic = np.array(Image.open('inputs/P1/the_magnificent_eleven_2.png'))

# # plt.imshow(image, cmap='gray')
# # plt.show()
#
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# from skimage import color, data, restoration
#
# rng = np.random.default_rng()
#
# # astro = color.rgb2gray(data.astronaut())
# from scipy.signal import convolve2d as conv2
# psf = np.ones((5, 5)) / 25
# astro = conv2(astro, psf, 'same')
# astro += 0.1 * astro.std() * np.random.standard_normal(astro.shape)
#
# deconvolved= restoration.wiener(astro, psf,1, clip=False)
#
# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 5),
#                        sharex=True, sharey=True)
#
# plt.gray()
#
# ax[0].imshow(astro)
# ax[0].axis('off')
# ax[0].set_title('Data')
#
# ax[1].imshow(deconvolved)
# ax[1].axis('off')
# ax[1].set_title('Self tuned restoration')
#
# fig.tight_layout()
#
# plt.show()

import cv2
import numpy as np

# imageeee = cv2.imread('inputs/P1/the_magnificent_eleven_2.png')
# src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

sharpen_kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(pic, -1, sharpen_kernel)
dst = cv2.equalizeHist(sharpen)
# dst = np.int_(((sharpen - sharpen.min()) / (sharpen.max() - sharpen.min())) * 255)
n= dst + pic
# n = np.int_(((n - n.min()) / (n.max() - n.min())) * 255)
# n = cv2.equalizeHist(n)

cv2.imshow('hhh', n)
cv2.waitKey()