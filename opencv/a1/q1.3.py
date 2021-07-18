import numpy as np
import cv2

img = cv2.imread("img.jpg")
cv2.imshow('original', img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

upper_col = np.array([130, 255, 255])
lower_col = np.array([90, 50, 20])
mask = cv2.inRange(hsv, lower_col, upper_col)
red = np.copy(img)
red[mask > 0] = (0, 0, 255)

cv2.imshow('red', red)
cv2.imwrite('red.jpg', red)

k = cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
