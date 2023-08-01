import numpy as np, cv2
from Common.utils import put_string		# 글쓰기 함수 임포트

capture = cv2.VideoCapture("chap04/images/move_file.avi")		# 동영상 파일 개방
if not capture.isOpened(): raise Exception("동영상 파일 개방 안됨")		# 예외 처리

while True: 
    ret, frame = capture.read()	# 카메라 영상 받기
    if not ret: break 
    
    x, y, w, h = (200, 100, 200, 100)
    cv2.rectangle(frame, (x,y,w,h), (0,0,255),2)
    tmp = frame[y:y+h, x:x+w]	
    # 함수 이용
    
average1 = tuple(map(int, cv2.mean(tmp)))

# 행렬 순회 방식
value = np.array([0,0,0], np.uint)
for row in tmp:
	for pixel in row:
		value += pixel
average2 = (value/(w*h)).astype(int)

put_string(frame, "average1:",(10,30), average1[:-1]) # 줌 값 표시
put_string(frame, "average2:", (10,60), average2) # 줌 값 표시
    
if cv2.waitKey(30) >= 0 : break
cv2.imshow("ex10",frame) # 윈도우에 영상 띄우기
capture.release()

