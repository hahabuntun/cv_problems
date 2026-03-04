import cv2

image = cv2.imread("../images/ela_original.jpg")

cv2.imshow("Original", image)

low_color = (0, 0, 150)

high_color = (255, 255, 255)

only_object = cv2.inRange(image, low_color, high_color)

cv2.imshow("only object", only_object)
cv2.waitKey(0)
