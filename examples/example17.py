import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("../images/gradient.png")
_, threshold1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) # if the value < 127 -> black, else white
_, threshold2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) # if the value < 127 -> white, else black
_, threshold3 = cv.threshold(img, 200, 255, cv.THRESH_TRUNC) # value <= 200 -> same value, else 200
_, threshold4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) # value <= 127 -> black, else the same value
_, threshold5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) # value >= 127 -> black, else the same value

titles = ["Original image", "binary", "binary inverse", "Trunc", "TOZERO", "TOZERO_INV"]

images = [img, threshold1, threshold2, threshold3, threshold4, threshold5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
