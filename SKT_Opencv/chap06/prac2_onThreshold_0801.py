import numpy as np
import cv2

def onChange(value):  
    alpha = cv2.getTrackbarPos('alpha', 'Result') / 100 
    beta = cv2.getTrackbarPos('beta', 'Result') / 100 
    add_img = cv2.addWeighted(image1, alpha, image2, beta, 0)
    result = cv2.hconcat([image1, add_img, image2])
    cv2.imshow('Result', result)

image1 = cv2.imread('C:/Users/033/sk_opencv/SKT_Opencv/chap06/images/add1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('C:/Users/033/sk_opencv/SKT_Opencv/chap06/images/add2.jpg', cv2.IMREAD_GRAYSCALE)

if image1 is None or image2 is None:
    raise Exception('영상파일 읽기 오류')

cv2.namedWindow('Result')
cv2.createTrackbar('alpha', 'Result', 0, 100, onChange) 
cv2.createTrackbar('beta', 'Result', 0, 100, onChange) 

alpha = cv2.getTrackbarPos('alpha', 'Result') / 100
beta = cv2.getTrackbarPos('beta', 'Result') / 100 
add_img = cv2.addWeighted(image1, alpha, image2, beta, 0)
result = cv2.hconcat([image1, add_img, image2])
cv2.imshow('Result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
