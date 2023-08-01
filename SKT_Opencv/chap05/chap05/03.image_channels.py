import cv2

image = cv2.imread( "chap05/chap05/images/color.jpg", cv2.IMREAD_COLOR)   # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")  # 예외 처리
if image.ndim != 3: raise Exception("컬러 영상 아님")
    
bgr = cv2.split(image)                      # 채널 분리: 컬러영상--> 3채널 분리
# blue, green, red = cv2.split(image)

print("bgr 자료형:", type(bgr), type(bgr[0]),type(bgr[0][0][0]))
print("bgr 원소개수:", len(bgr))

# 각 채널을 윈도우에 띄우기 
cv2.imshow("image", image)
cv2.imshow("blue channel", bgr[0]) # 파랑 채널
cv2.imshow("green channel", bgr[1]) # 초록 채널
cv2.imshow("red channel", bgr[2]) # 빨강 채널
# cv2.imshow("image", image)
cv2.waitKey()