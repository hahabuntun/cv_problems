import numpy as np
import cv2

capImg = cv2.VideoCapture(0)

while(capImg.isOpened()):
    ret, frame = capImg.read()

    if frame is None:
        break

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    crop_frame = frame[60:270, 30:750]
    crop_frame_hsv = frame_hsv[60:270, 30:750]

    low_blue = np.array([105, 150, 0], dtype="uint8")
    high_blue = np.array([50, 255, 210], dtype="uint8")

    low_yel = np.array([10, 150, 100], dtype="uint8")
    high_yel = np.array([135, 255, 255], dtype="uint8")

    low_red_orange = np.array([0, 85, 110], dtype="uint8")
    high_red_orange = np.array([5, 165, 155], dtype="uint8")

    low_red_violet = np.array([165, 55, 40], dtype="uint8")
    high_red_violet = np.array([180, 105, 120], dtype="uint8")

    blue_mask = cv2.inRange(crop_frame_hsv, low_blue, high_blue)
    yel_mask = cv2.inRange(crop_frame_hsv, low_yel, high_yel)
    red_orange_mask = cv2.inRange(crop_frame_hsv, low_red_orange, high_red_orange)
    red_violet_mask = cv2.inRange(crop_frame_hsv, low_red_violet, high_red_violet)

    full_mask = blue_mask + yel_mask + red_orange_mask + red_violet_mask

    cv2.imshow("video mask", full_mask)
    cv2.imshow("video_frame", crop_frame)

    key_press = cv2.waitKey(30)

    if key_press == ord("q"):
        break

capImg.release()
cv2.destroyAllWindows()
