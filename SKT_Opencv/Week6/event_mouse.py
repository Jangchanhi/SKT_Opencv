import numpy as np
import cv2

def onMouse(event, x, y, flags, param):     # 콜백 함수 
    if event == cv2.EVENT_LBUTTONDOWN:
        print("바우스 왼쪽 버른 누름")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("바우스 오른쪽 버른 누름")
    elif event == cv2.EVENT_RBUTTONUP:
        print("바우스 오른쪽 버른 떼기")
    elif event == cv2.EVENT_LBUTTONUP:
        print("바우스 왼쪽 버른 떼기")

image = np.full((200,300), 255, np.uint8)       # 영상 생성

title1, title2 = "Mouse Event1", "Mouse Event2" #윈도우 이름
cv2.imshow(title1, image)   # 영상 보기
cv2.imshow(title2, image)   # 영상 보기

cv2.setMouseCallback('Mouse Event1',onMouse)    # 마우스 콜백 함수

cv2.waitKey(0)      # 키 이벤트 대기
cv2.destroyAllWindows()     # 열린 모든 윈도우 제거












