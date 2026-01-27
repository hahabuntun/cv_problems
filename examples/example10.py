import numpy as np
import cv2 as cv

def do_nothing(x):
    print(x)

img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, do_nothing)
cv.createTrackbar('G', 'image', 0, 255, do_nothing)
cv.createTrackbar('R', 'image', 0, 255, do_nothing)

switch = '0 : OFF\n 1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, do_nothing)

while True:
    cv.imshow('image', img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
    
cv.destroyAllWindows()