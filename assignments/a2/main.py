import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    width = int(cap.get(3))
    height = int(cap.get(4))
    # image = np.zeros(frame.shape, np.uint8)
    # smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # image[height//2:, :width//2] = smaller_frame
    # image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # image[height//2:, width//2:] = smaller_frame

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # upper_col = np.array([20, 150, 255])
    # lower_col = np.array([0, 10, 60])
    upper_col = np.array([130, 255, 255])
    lower_col = np.array([90, 50, 50])
    mask = cv2.inRange(hsv, lower_col, upper_col)
    red = np.copy(frame)
    red[mask > 0] = (0, 0, 255)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    # cv2.imshow('frame', image)
    # cv2.imshow('frame', cv2.resize(frame, (0,0), fx = 1/2, fy = 1/2))
    # cv2.imshow('frame', frame)
    # cv2.imshow('frame', frame)
    cv2.imshow('final', result)
    cv2.imshow('mask', mask)
    cv2.imshow('original', frame)
    cv2.imshow('red', red)


    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)