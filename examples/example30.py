import numpy as np
import cv2

file_name = "../images/rec_img1.png"

img = cv2.imread(file_name)

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hsv_min = np.array((90, 100, 100), np.uint8)
hsv_max = np.array((120, 255, 200), np.uint8)

hsv_mask = cv2.inRange(hsv_img, hsv_min, hsv_max)

contours, hierarchy = cv2.findContours(hsv_mask,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    rect = cv2.minAreaRect(contour)

    area = int(rect[1][0] * rect[1][1])

    if area > 500:
        box = cv2.boxPoints(rect)

        box = box.astype(int)

        cv2.drawContours(img, [box], -1, (255, 0, 0), 3)

cv2.imshow("contours", img)

cv2.waitKey()
cv2.destroyAllWindows()