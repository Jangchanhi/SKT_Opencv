# 글자쓰기 4.3.2

import numpy as np
import cv2

olive, violet, brown = (128, 128, 0), (221, 160, 221), (42, 42, 165) # 생상 지정
pt1, pt2 = (50, 230), (50, 310)

image = np.zeros((350, 500, 3), np.uint8)
image.fill(255)

cv2.putText(image, 'Simple', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, brown)
cv2.putText(image, 'DUPLEX', (50,130), cv2.FONT_HERSHEY_DUPLEX, 3, olive)
cv2.putText(image, 'TRIPLEX', pt1, cv2.FONT_HERSHEY_TRIPLEX, 2, violet)
fontFace = cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC
cv2.putText(image, 'ITALIC', pt2, fontFace, 4, violet)
# fontFace - cav

cv2.imshow('Put Text',image)
cv2.waitKey(0)
cv2.destroyAllWindows()         # 모든 윈도우 닫기















