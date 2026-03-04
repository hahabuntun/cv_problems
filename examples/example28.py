import numpy as np
import cv2

file_name = "../images/ball_ball.png"

img = cv2.imread(file_name)

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hsv_min = np.array((2, 28, 65), np.uint8)
hsv_max = np.array((26, 238, 255), np.uint8)

hsv_mask = cv2.inRange(hsv_img, hsv_min, hsv_max)

contours, hierarchy = cv2.findContours(hsv_mask,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (255, 0, 0),
                 3, cv2.LINE_AA, hierarchy, 2)

cv2.imshow("countours", img)
cv2.waitKey()
cv2.destroyAllWindows()