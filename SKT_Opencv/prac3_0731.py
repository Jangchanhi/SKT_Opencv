import numpy as np, cv2


def onChange(x):
    global title
    global image
    pt = x
    
    add_value = x + add_value 
    add_value = y + add_value
    print("추가 픽셀값:", add_value)
    image = image + add_value
    cv2.imshow(title, image)

def onMouse(event, x, y, flags, param):
    global title
    global image
    pt = (x,y)

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, pt, 20, 100, 2)
        cv2.imshow(title, image)
    elif event == cv2.EVENT_LBUTTONDOWN:
        pt2 = (pt[0]+30 , pt[1]+30)
        cv2.rectangle(image, pt, pt2, 100, 2)
        cv2.imshow(title, image)

image = np.ones((300, 300), np.uint8)*255
title = "ex10"
cv2.imshow(title, image)
cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)













