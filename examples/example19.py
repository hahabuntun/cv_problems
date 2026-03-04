"""smoothing images/blurring images"""
# low pass filters help remove the noise(or blurring the image)
# high pass filters help to find edges

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("../images/lena.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25
destination = cv2.filter2D(img, -1, kernel) # smoothen the image
blur = cv2.blur(img, (5, 5))
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5) # helps with salt and peper noise
bilateralFitler = cv2.bilateralFilter(img, 9, 75, 75)

titles = ["image", "2d convolution", "blur", "gaus_blur", "median"]
images = [img, destination, blur, gaussian_blur, median]

for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
