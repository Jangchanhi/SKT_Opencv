import numpy as np, cv2

def onChange(value):
    global image, title, a

    a = value


def onMouse(event, x, y, flags, param):
    global title, image
    pt = (x, y)

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, pt, 20+a, 150, 2)
        cv2.imshow(title, image)

    elif event == cv2.EVENT_LBUTTONDOWN:
        pt2 = (pt[0] + (30+a), pt[1] + (30+a))
        cv2.rectangle(image, pt, pt2, 10, 2)
        cv2.imshow(title, image)

image = np.ones((300, 300), np.uint8) * 255
title = "ex10"
cv2.imshow(title, image)
cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)