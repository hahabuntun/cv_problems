# thresholding

import cv2 as cv

img = cv.imread("../images/gradient.png")
_, threshold1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) # if the value < 127 -> black, else white
_, threshold2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) # if the value < 127 -> white, else black
_, threshold3 = cv.threshold(img, 200, 255, cv.THRESH_TRUNC) # value <= 200 -> same value, else 200
_, threshold4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) # value <= 127 -> black, else the same value
_, threshold5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) # value >= 127 -> black, else the same value

cv.imshow('Image', img)
cv.imshow('Th1', threshold1)
cv.imshow('Th2', threshold2)
cv.imshow('Th3', threshold3)
cv.imshow('Th4', threshold4)
cv.imshow('Th5', threshold5)

cv.waitKey(0)
cv.destroyAllWindows()