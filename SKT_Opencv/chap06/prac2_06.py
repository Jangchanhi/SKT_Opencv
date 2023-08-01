# import cv2
# import numpy as np
# def onThreshold(value):

#     # THRESH_BINARY, TRESH_BINARY_INV, THRESH_TOZERO, THRESH_TOZERO_INV
#     global alpha, beta, dst
#     alpha = value/255
#     beta = 1- alpha
#     dst [:, w:2*w] = cv2.addWeighted(src1 = horse,alpha = alpha, src2 = other, beta=beta, gamma = 0)
#     cv2.imshow("result", dst)

# alpha = beta = 0.5
# horse = cv2.imread(r'C:/Users/033/sk_opencv/SKT_Opencv/chap06/images/add1.jpg', cv2.IMREAD_GRAYSCALE)
# other = cv2.imread(r'C:/Users/033/sk_opencv/SKT_Opencv/chap06/images/add2.jpg', cv2.IMREAD_GRAYSCALE)
# h, w = horse.shape


# dst = cv2.repeat(horse, 1, 3)
# result = np.zeros(horse.shape, np.uint8)
# dst [:, 2*w: w*3] = other
# cv2.namedWindow("result")
# cv2.imshow("result", dst)
# cv2.createTrackbar("alpha/beta", "result", 0, 255, onThreshold)
# cv2.waitKey(0)

import numpy as np, cv2

image1 = cv2.imread("C:/Users/033/sk_opencv/SKT_Opencv/chap06/images/add1.jpg", cv2.IMREAD_GRAYSCALE)   # 영상 읽기
image2 = cv2.imread("C:/Users/033/sk_opencv/SKT_Opencv/chap06/images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")

def drawing(a,b):
    global image1, image2
    add_img3 = cv2.addWeighted(image1, a, image2, b,0)
    dst = np.hstack((image1, add_img3,image2))
    cv2.imshow('dst',dst)

def onChangeL(value): # 왼쪽 그림 처리
    global a,b
    a=value/100
    drawing(a,b)

def onChangeR(value):   # 오른쪽 그림 처리
    global a,b
    b=value/100
    drawing(a,b)

a,b=0.5, 0.5
drawing(a,b)
cv2.createTrackbar("left", 'dst', 50, 100, onChangeL)
cv2.createTrackbar("right", 'dst',50, 100, onChangeR)
cv2.waitKey(0)

