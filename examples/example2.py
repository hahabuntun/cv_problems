"""Capture video and save it to file"""
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter.fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter("../output/example2.avi", fourcc, 20, (640, 480))


while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # frame width
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # frame heigh

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()