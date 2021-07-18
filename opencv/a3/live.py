import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    width = int(cap.get(3))
    height = int(cap.get(4))

    cv2.imshow('original', img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)

    blurred = cv2.GaussianBlur(255 - gray, ksize=(41, 41),
                               sigmaX=10, sigmaY=10)
    cv2.imshow('blurred', blurred)

    def dodge(image, mask):
        return cv2.divide(image, 255 - mask, scale=256)

    final = dodge(gray, blurred)

    cv2.imshow('final', final)
    cv2.imshow('original', img)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)