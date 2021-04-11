import numpy as np
import cv2

img = cv2.imread("img.png")
img = cv2.resize(img, (200, 200))
height, width, _ = img.shape

smaller_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

image = np.zeros(img.shape, np.uint8)
image[:height//2, :width//2] = smaller_img
cv2.imshow("1", image)

image = np.zeros(img.shape, np.uint8)
image[height//2:, :width//2] = smaller_img
cv2.imshow("2", image)

image = np.zeros(img.shape, np.uint8)
image[:height//2, width//2:] = smaller_img
cv2.imshow("3", image)

image = np.zeros(img.shape, np.uint8)
image[height//2:, width//2:] = smaller_img
cv2.imshow("4", image)

image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("5", image)

image = np.zeros(img.shape, np.uint8)
image[height//2:, :width//2] = cv2.rotate(smaller_img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("6", image)

image = np.zeros(img.shape, np.uint8)
image[:height//2, width//2:] = cv2.rotate(smaller_img, cv2.ROTATE_180)
cv2.imshow("7", image)

image = np.zeros(img.shape, np.uint8)
image[height//2:, width//2:] = cv2.rotate(smaller_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("8", image)


image = cv2.GaussianBlur(img, ksize=(7, 7),
                           sigmaX=10, sigmaY=10)
cv2.imshow("9", image)

image = cv2.medianBlur(img, 7)
cv2.imshow("10", image)

cv2.imshow("original", img)

k = cv2.waitKey(0)
cv2.destroyAllWindows()