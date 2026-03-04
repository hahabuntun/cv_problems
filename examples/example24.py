import numpy as np

import cv2

cap_img = cv2.VideoCapture(0)

while (True):
    ret, frame = cap_img.read()

    if frame is None:
        break

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    crop_frame = frame[60:270, 30:750]
    crop_frame_hsv = frame_hsv[60:270, 30:750]

    low_blue = np.array([105, 150, 0], dtype="uint8")
    high_blue = np.array([135, 255, 210], dtype="uint8")

    blue_mask = cv2.inRange(crop_frame_hsv, low_blue, high_blue)

    cv2.imshow("video_mask", blue_mask)
    cv2.imshow("video_frame", crop_frame)

    key_press = cv2.waitKey(30)
    if key_press == ord("q"):
        break

cap_img.release()
cv2.destroyAllWindows()
