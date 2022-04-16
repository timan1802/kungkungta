import cv2

imageFile = '../img/test1.png'

img = cv2.imread(imageFile)
img2 = cv2.imread(imageFile, 0)
img3 = cv2.imread(imageFile, -1)

cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img2)
cv2.imshow('Lena alpha channel', img3)

cv2.waitKey(5000)  # 5초 후에 자동 close, 빈 칸이면 아무 키 누르면 close
cv2.destroyAllWindows()