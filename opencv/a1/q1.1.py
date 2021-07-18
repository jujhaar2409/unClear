import cv2

img = cv2.imread('img.jpg')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, bnw) = cv2.threshold(grey, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('original', img)
cv2.imshow('black and white', bnw)
cv2.imwrite('bnw.jpg', bnw)
cv2.imshow('grey', grey)
cv2.imwrite('grey.jpg', grey)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
