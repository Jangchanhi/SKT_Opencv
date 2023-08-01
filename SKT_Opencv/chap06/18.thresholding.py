import cv2

def onThreshold(value):
    result = cv2.threshold(image, value, 255, cv2.THRESH_TOZERO_INV)[1]
    cv2.imshow("result", result)

image = cv2.imread("C:/Users/033/sk_opencv/SKT_Opencv/chap06/images/color_space.jpg", cv2.IMREAD_GRAYSCALE) # 컬러 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")

cv2.namedWindow("result")
cv2.createTrackbar("threshold", "result", 128, 255, onThreshold)
# cv2.THRESH_BINARY_INV("thresh_binary_inv", "result", 128, 200, onThreshold)
# cv2.THRESH_TOZERO("thresh_tozero", "result", 128, 200, onThreshold)
# cv2.THRESH_TOZERO_INV("thresh_tozero_inv", "result", 128, 200, onThreshold)

onThreshold(128)
cv2.imshow("image", image)
cv2.waitKey(0)