import numpy as np, cv2

image1 = cv2.imread("C:/Users/033/sk_opencv/SKT_Opencv/chap06/images/add1.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image1 is None: raise Exception("영상 파일 읽기 오류 발생")

image2 = cv2.imread("C:/Users/033/sk_opencv/SKT_Opencv/chap06/images/add2.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image2 is None: raise Exception("영상 파일 읽기 오류 발생")

noimage = np.zeros(image1.shape[:2], image1.dtype)        # 더미 영상
avg = cv2.mean(image1)[0]/2.0

alpha, beta = 0.6, 0.7

add_img = cv2.addWeighted(image1, alpha, image2, beta, 0)

result = cv2.hconcat([image1, add_img, image2])

cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()












