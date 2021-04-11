import cv2
import numpy as np

img = cv2.imread("img.jpg", 1)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

cv2.imshow('grey scale', img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

steps = 20
mid = 150

for i in range(1, steps + 1):
    black_upper = np.array([255, 255, mid * i / steps])
    black_lower = np.array([0, 0, mid * (i - 1) / steps])
    black_mask = cv2.inRange(hsv, black_lower, black_upper)
    if i > steps // 3:
        img[black_mask > 0] = [mid * (i) / steps] * 3
    else:
        img[black_mask > 0] = [0] * 3

white_upper = np.array([255, 255, 255])
white_lower = np.array([0, 0, mid])
white_mask = cv2.inRange(hsv, white_lower, white_upper)

img[white_mask > 0] = [255, 255, 255]

cv2.imshow('black and white', img)
