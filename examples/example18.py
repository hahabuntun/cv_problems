# morphological transformations
import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("../images/smarties.png", cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((2, 2), np.uint8)
dilation = cv2.dilate(mask, kernel, iterations=4)
erosion = cv2.erode(mask, kernel, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # erosion + dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) # dilation + erosion
m_gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel) # difference between dilation and erosion
m_tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel) # difference between input and opening



titles = ["image", "mask", "dilation", "erosion", "opening", "closing", "gradient", "tophat"]
images = [img, mask, dilation, erosion, opening, closing, m_gradient, m_tophat]

for i in range(len(images)):
    plt.subplot(2, 4, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
