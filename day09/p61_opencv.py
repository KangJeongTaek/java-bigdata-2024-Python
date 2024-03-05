# file : p61_opencv.py
# desc : OpenCV 계속

import cv2

image = cv2.imread('./images/coby.jpg',cv2.IMREAD_UNCHANGED)
dst = cv2.blur(image,ksize=(9,19),anchor=(-1,-1),borderType=cv2.BORDER_DEFAULT)

height,width,channel = image.shape
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
sobel = cv2.Sobel(gray,cv2.CV_8U,1,0,3)
laplacian = cv2.Laplacian(gray,cv2.CV_8U,ksize=3)
canny = cv2.Canny(image,100,255)

cv2.imshow('Coby the cat',image)

cv2.imshow('Blur',dst) #블러 이미지

cv2.imshow('Sobel',sobel) # 입체감이 있는 윤각

cv2.imshow('Laplacian',laplacian) # 일반적인 윤각따기

cv2.imshow('Canny',canny) # 흑백으로 윤곽따기

cv2.waitKey(0)

cv2.destroyAllWindows()