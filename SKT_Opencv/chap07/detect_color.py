import cv2
import numpy as np
import random

# 이미지 불러오기
image = cv2.imread('./chap07/images/test_color.jpg')
image = np.ones((480, 640, 3), dtype="uint8") *255

def draw_circle(iamge, color, radius, count):
    # 원의 위치가 겹치지 않도록 중복 없이 좌표 생성
    positions = set()

    while len(positions) < count:
        # 반지름만큼의 여유를 두고 좌표를 랜덤하게 생성
        x = random.randint(radius, image.shape[1] - radius)
        y = random.randint(radius, image.shape[0] - radius)

        if (x,y) not in positions:
            cv2.circle(image, (x,y), radius, color, -1)
            positions.add((x,y))
            
# 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지를 블러 처리하여 노이즈 제거
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 원을 탐지하기 위해 Hough Circle 변환 적용
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=30, minRadius=5, maxRadius=100)

# 색깔 구별을 위한 mapping 설정
mapping = {0: 'blue', 1:'green' , 2:'red'}

# 원이 탐지되었을 경우에만 실행
if circles is not None:
    
    # 원의 중심 좌표와 반지름 값을 반올림하여 정수로 변환
    circles = np.round(circles[0, :]).astype("int")

    # 각 원에 대해 반복
    for (x, y, r) in circles:
        # 원 주위에 사각형 박스 그리기
        cv2.rectangle(image, (x - r, y - r), (x + r, y + r), (50, 50, 50), 2)

        # 원의 색상 정보 텍스트로 표시
        color = image[y, x]
        text = f'{mapping[np.argmax(color)]}'
        
        cv2.putText(image, text, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
else : print("원을 찾을 수 없습니다")

# 결과 이미지 출력
cv2.imshow("Circle Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()



