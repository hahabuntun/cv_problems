import cv2
import numpy as np


def do_nothing(x):
    print(x)


cap = cv2.VideoCapture(0)

cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, do_nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, do_nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, do_nothing)
cv2.createTrackbar('UH', 'Tracking', 255, 255, do_nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, do_nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, do_nothing)


while True:
    _, frame = cap.read() 

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_hue = cv2.getTrackbarPos('LH', 'Tracking')
    lower_saturation = cv2.getTrackbarPos('LS', 'Tracking')
    lower_value = cv2.getTrackbarPos('LV', 'Tracking')
    upper_hue = cv2.getTrackbarPos('UH', 'Tracking')
    upper_saturation = cv2.getTrackbarPos('US', 'Tracking')
    upper_value = cv2.getTrackbarPos('UV', 'Tracking')
    lower_blue_color = np.array([lower_hue, lower_saturation, lower_value])
    upper_blue_color = np.array([upper_hue, upper_saturation, upper_value])

    mask = cv2.inRange(hsv, lower_blue_color, upper_blue_color )
    res = cv2.bitwise_and(frame, frame, mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()