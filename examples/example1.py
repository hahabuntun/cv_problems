import cv2

img = cv2.imread('../images/lena.jpg', 0)


cv2.imshow('image', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

cv2.imwrite('lena_copy.png', img)