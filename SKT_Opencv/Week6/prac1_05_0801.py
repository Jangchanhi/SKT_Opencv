import numpy as np, cv2

image = cv2.imread("C:/Users/033/sk_opencv/SKT_Opencv/chap05/chap05/images/color.jpg")
if image is None: raise Exception("영상 파일 읽기 오류")

mask = np.zeros(image.shape[:2], np.uint8)
center = (190, 170)
size = (100, 50)  # 타원의 크기를 임의로 설정합니다. 실제 사용할 때는 적절한 값을 선택해야 합니다.

# 타원형 마스크를 생성합니다.
cv2.ellipse(mask, center, size, 0, 0, 360, 255, -1)

# 마스크를 적용하여 원본 이미지에서 타원 영역만 추출합니다.
masked_image = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Masked Image", masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

