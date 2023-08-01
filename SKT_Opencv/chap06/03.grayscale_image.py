import numpy as np, cv2

image1 = np.zeros((50, 512), np.uint8)         # 50 x 512 영상 생성
image2 = np.zeros((50, 512), np.uint8)

rows, cols = image1.shape[:2]





cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.waitKey(0)