import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    width = int(cap.get(3))
    height = int(cap.get(4))

    cv2.imshow('original', frame)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)