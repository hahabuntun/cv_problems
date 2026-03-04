import cv2
from matplotlib import pyplot as plt

img = cv2.imread("../images/lena.jpg")

cv2.imshow('image', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([]) # hide x ticks
plt.yticks([]) # hied y ticks
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()