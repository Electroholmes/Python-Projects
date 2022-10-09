import cv2
import numpy as np
def sketch(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur_gray = cv2.GaussianBlur(gray,(5,5),900)
    edges = cv2.Canny(blur_gray,45,90)
    ret,thre = cv2.threshold(edges,70,255,cv2.THRESH_BINARY_INV)
    return thre
cam = cv2.VideoCapture(0)
while 1:
    ret,frame = cam.read()
    cv2.imshow('Live Sketch', sketch(frame))
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==13:
        cv2.imwrite('sketch.jpg',sketch(frame))
        print('Image Saved!!!')
cam.release()
cv2.destroyAllWindows()