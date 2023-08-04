import cv2
import numpy as np
import pytesseract

TESSERACT_PATH = ""

def onMouse(event, x, y, flags, param):
    global img, selected_points

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 5, (200, 50, 50), -1)    # 클릭한 점에 대해 원으로 표시
        cv2.imshow(win_name, img)
        if len(selected_points) <4:
            selected_points.append((x,y))
        if len(selected_points) == 4:
            cv2.setMouseCallback(win_name, lambda *args: None)
            CropAndProcessImage(selected_points)

    return 0

# 이미지 크롭 및 필터링
def CropAndProcessImage(pts):
    global img 
    if len(pts) !=4:
        print("Please select exactly four points.")
        return
    
    pts_arr = np.array(pts, np.float32) # 실수 넘파이 배열로 변환

    orderd_points = orderd_points(pts_arr) # 좌표 정렬

    # 마우스로 잡은 네개의 점에서 직사각형으로 만들 목표 이미지의 width, heigh를 계산
    target_width = int(max(np.linalg.norm(orderd_points[0] - orderd_points[1]), np.linalg.norm(orderd_points[2] - orderd_points[3])))
    target_height = int(max(np.linalg.norm(orderd_points[0] - orderd_points[3]), np.linalg.norm(orderd_points[1] - orderd_points[2])))

    # 목표 이미지의 네개의 좌표 정의
    target_points = np.array([[0,0], [target_width, 0], [target_width, target_height], [0, target_height]], np.float32)               

    # 원근 변환(크롭된 이미지가 직사각형이 되도록 변환함) 행렬을 계산 및 크롬
    M = cv2.getPerspectiveTransform(orderd_points, target_points)
    cropped_img = cv2.warpPerspective(img, M, (target_width, target_height))

    # 가우시안 블러를 이용하여 필터링
    gray_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
    filtered_img = cv2.GaussianBlur(gray_img, (3,3),0)    


# OCR function
def GetOCR(img):
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
    text = pytesseract.image_to_string(img, lang='kor+eng')
    return text

#이미치 처리 함수
def ImgProcessing():
    
    return 0

# 원근 변환을 위한 좌표 정렬 함수
def order_points(pts):
    rect = np.zeros((4,2), dtype=np.float32)

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmin(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmin(diff)]
    return rect

# 입력 이미지가 큰 경우를 대비하여 윈도우 크기 고정
def SetWindowFixedSize(winname, width, height):
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(winname, width, height)
    return winname, width, height

#OCR 함수
def GetOCR(img):
    #이미지 불러오기
    # global img

    #OCR모델 불러오기
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

    #OCR모델로 글자 추출
    text = pytesseract.image_to_string(img, lang='kor+eng')
        
    return text

SetWindowFixedSize(win_name, 800, 600)

cv2.imshow(win_name, img)   #이미지 출력

cv2.waitKey(0)              #입력 대기
text = GetOCR()             #OCR함수로 텍스트 추출
print(text)                 #텍스트 출력