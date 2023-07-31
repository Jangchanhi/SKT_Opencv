import numpy as np
import cv2

# 검정색 이미지 하나 생성
image = np.zeros((200,300), np.uint8)

image.fill(255)

# 
title1, title2 = 'AUTOSIZE', 'NORMAL'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)

cv2.imshow(title1, image)
cv2.imshow(title2, image)

cv2.moveWindow(title1, 400, 300)
cv2.moveWindow(title2, 400, 300)

# 이미지를 기다림
cv2.waitKey(0)
cv2.destroyAllWindows()
