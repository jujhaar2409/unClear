import cv2

img = cv2.imread("img.jpg", 1)

cv2.imshow('original', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

blurred = cv2.GaussianBlur(255 - gray, ksize=(41, 41),
                            sigmaX=10, sigmaY=10)
cv2.imshow('blurred', blurred)

def dodge(image, mask):
    return cv2.divide(image, 255-mask, scale=256)

final = dodge(gray, blurred)

cv2.imshow('sketch', final)
cv2.imwrite('sketch.jpg', final)

cv2.waitKey(0)
cv2.destroyAllWindows()
