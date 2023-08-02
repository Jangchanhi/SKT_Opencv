import numpy as np, cv2

image = cv2.imread("./chap07/images/test_color.jpg")
if image is None: raise Exception("영상파일 읽기 오류")

# gray 색상으로 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 잡음을 제거
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# 원 검출을 위한 파라미터 설정
# 이 값들은 이미지에 따라 조정할 필요가 있을 수 있습니다.
dp = 1         # 검출 해상도 비율 (1: 동일 해상도)
minDist = 50   # 감지된 원들의 최소 중심 간격
param1 = 50    # Canny 에지 검출기 파라미터1
param2 = 30    # 원 검출을 위한 임계값
minRadius = 10  # 검출할 원의 최소 반지름 크기
maxRadius = 100 # 검출할 원의 최대 반지름 크기

# Hough Circle Transform을 사용하여 원 검출
circles = cv2.HoughCircles(blurred_image, cv2.HOUGH_GRADIENT, dp, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

if circles is not None:
    # 원이 검출된 경우 좌표와 반지름을 정수로 변환
    circles = np.round(circles[0, :]).astype("int")

    # 검출된 원 정보를 기반으로 상자 모양 검출
    for (x, y, r) in circles:
        # 원의 중심을 기준으로 상자의 좌상단과 우하단 좌표 계산
        x1 = x - r
        y1 = y - r
        x2 = x + r
        y2 = y + r

        # 원 주변에 상자를 그립니다.
        color = tuple(image[y, x])
        color_name = ['blue','green','red']
        text_x = x - r
        text_y = y - r - 3
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.7
        thickness = 2
        
        max_value = max(color)  # 리스트에서 가장 큰 값(20) 찾기
        max_index = color.index(max_value)  # 가장 큰 값(20)의 인덱스(6) 찾기
        
        cv2.rectangle(image, (x1, y1), (x2, y2), (int(color[0]),int(color[1]),int(color[2])), 2)
        cv2.putText(image, color_name[max_index], (text_x, text_y), font, font_scale, (int(color[0]),int(color[1]),int(color[2])), thickness)

    # 결과 이미지 출력
    cv2.imshow("Detected Boxes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("원을 찾을 수 없습니다.")


