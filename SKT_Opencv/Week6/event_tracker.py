import numpy as np
import cv2
def onChange(value):
    global image, title

    add_value = value - int(image[0][0])
    print("추가 화소값:", add_value)
    image = image + add_value
    cv2.imshow(title, image)

image = np.zeros((300, 500), np.uint8)

title = 'Tracker Event'
cv2.imshow(title, image)

cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)
cv2.waitKey(0)

# 한번만 작동되게 말고 계속 밝기 조절 가능하도록 하기
# while True:         # 무한 반복
#     key = cv2.waitKeyEx(100)    # 100ms 동안 키 이벤트 대기
#     if key == 27: break     # ESC 키 누르면 종료

#     try:
#         result = switch_case[key]
#         print(result)
#     except KeyError:
#         result = -1

cv2.destroyAllWindows()     # 열린 모든 윈도우 제거