import numpy as np
import cv2

# 검정색 이미지 하나 생성
image = np.zeros((200,300), np.uint8)

# 밝은 회색으로 채운다.(아무 색이나 상관없음)
image[:]=150

# 
title1, title2 = 'Position1', 'Position2'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2, cv2.WINDOW_AUTOSIZE)
cv2.moveWindow(title1, 150, 150)
cv2.moveWindow(title2, 400, 50)

cv2.imshow(title1, image)
cv2.imshow(title2, image)

# 이미지를 기다림
cv2.waitKey(0)
cv2.destroyAllWindows()
