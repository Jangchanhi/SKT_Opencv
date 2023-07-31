import cv2
print(cv2.__version__)
# 이미지의 시각화
from google.colab.patches import cv2_imshow

# 이미지의 경로 복사
path = 'C:\Users\033\sk_opencv\data\lie.png'

image = cv2.imread(path, cv2.IMREAD_COLOR) # 영상을 읽을 떄 컬러로 가져오겠다.

print(cv2_imshow(image))
# opencv는 BGR로 읽는다.

image = cv2.imread(path, cv2.IMREAD_GRAYSCALE) # 영상을 읽을 떄 컬러로 가져오겠다.

if image is not None:
    cv2_imshow(image)
else:
    print('NO image file')

print(cv2_imshow(image))

# 이미지 영상 밝기 변화
dst1 = cv2.add(image, 200)
dst2 = cv2.subtract(image,100)

print(cv2_imshow(image))
print(cv2_imshow(dst1))
print(cv2_imshow(dst2))

# test2.jpg로 이미지 저장
cv2.imwrite('/content/test2.png', dst2)
# cv2.imwrite('/content/lie.png'.dst2

print(cv2_imshow(dst2))





