import cv2

image = cv2.imread("../images/YellowBall.jpeg")
cv2.imshow("Original", image)

hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
color_low = (35, 40, 40)
color_high = (85, 255, 255)
only_object = cv2.inRange(hsv_img, color_low, color_high)
cv2.imshow('color hsv', only_object)

cv2.waitKey(0)