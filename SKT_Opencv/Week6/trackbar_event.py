import numpy as np
import cv2

def onChange(value):
    global image, title             # 전역 변수 참조

    add_value = value - int(image[0][0])
    image[:] = image + add_value        # 트렉바 값과 영상화소값 차분
    cv2.imshow(title, image)

def onMouse(event, x, y, flags, param):
    global image, bar_name

    if event == cv2.EVENT_RBUTTONDOWN:
        if (image[0][0] < 246): image[:] = image + 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)
    
    elif event ==cv2.EVENT_LBUTTONDOWN:
        if (image[0][0] >=10): image[:] = image - 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])    
        cv2.imshow(title, image)


image = np.zeros((300, 500), np.uint8)

title = "Trackbar & Mouse Event"    # 윈도우 이름
bar_name = "Brightness"
cv2.imshow(title, image)        # 트렉바 이름

cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange) # 트랙바 콜백 함수
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)      # 키 입력 대기
cv2.destroyAllWindows()         # 모든 윈도우 닫기

# 한번만 작동되게 말고 계속 밝기 조절 가능하도록 하기
# while True:         # 무한 반복
#     key = cv2.waitKeyEx(100)    # 100ms 동안 키 이벤트 대기
#     if key == 27: break     # ESC 키 누르면 종료

#     try:
#         result = switch_case[key]
#         print(result)
#     except KeyError:
#         result = -1

# cv2.destroyAllWindows()     # 열린 모든 윈도우 제거