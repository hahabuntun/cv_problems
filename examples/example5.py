import datetime

import cv2
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"Width {cap.get(cv2.CAP_PROP_FRAME_WIDTH)} " \
            f"Height: {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}"

        frame = cv2.putText(frame, current_date, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()