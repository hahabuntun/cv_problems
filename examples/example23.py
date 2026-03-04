import cv2

captured_image = cv2.VideoCapture(0)

while True:
    ret, frame = captured_image.read()

    cv2.imshow("Video", frame)
    key_press = cv2.waitKey(30)

    if key_press == ord('q'):
        break

captured_image.release()
cv2.destroyAllWindows()