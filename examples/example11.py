import numpy as np
import cv2 as cv


def do_nothing(x):
    print(x)


cv.namedWindow('image')

cv.createTrackbar('CP', 'image', 10, 400, do_nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, do_nothing)

while True:
    img = cv.imread('../images/lena.jpg')
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 4, (0, 0, 255))

    key = cv.waitKey(10) & 0xFF
    if key == 27:
        break

    s = cv.getTrackbarPos(switch, 'image')

    if s != 0:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    img = cv.imshow('image', img)



cv.destroyAllWindows()