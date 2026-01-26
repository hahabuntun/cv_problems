"""
Read an image from a file and write an image to a file
"""
import cv2

img = cv2.imread('../images/lena.jpg', 0)

cv2.imshow('image', img)

key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()
