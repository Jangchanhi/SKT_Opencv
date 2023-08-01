import numpy as np, cv2
from Common.filters import filter

image = cv2.imread("C:/Users/033/sk_opencv/SKT_Opencv/chap07/images/filter_sharpen.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상파일 읽기 오류")

# 샤프닝 마스크 원소 지정 
data1 = [[0,-1,0],[-1,5,-1],[0,-1,0]]
data2 = [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
data3 = [[-1,0,-1],[0,5,0],[-1,0,-1]]

mask1 = np.array(data1, np.float32).reshape(3, 3)
mask2 = np.array(data2, np.float32)
mask3 = np.array(data3, np.float32).reshape(3,3)

sharpen1 = filter(image, mask1)
sharpen2 = filter(image, mask2)
sharpen3 = filter(image, mask3)

sharpen1 = cv2.convertScaleAbs(sharpen1)
sharpen2 = cv2.convertScaleAbs(sharpen2)
sharpen3 = cv2.convertScaleAbs(sharpen3)

cv2.imshow("image", image)
cv2.imshow("sharpen1", cv2.convertScaleAbs(sharpen1))  # 윈도우 표시 위한 형변환
cv2.imshow("sharpen2", cv2.convertScaleAbs(sharpen2))
cv2.imshow("sharpen3", cv2.convertScaleAbs(sharpen3))

cv2.waitKey(0)