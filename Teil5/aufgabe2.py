import cv2
import numpy as np
width=1
height=1
grad = 0
def drehen_links():
    global grad
    grad = grad-90
    rows,cols = img.shape[:2]
    M=cv2.getRotationMatrix2D((cols/2,rows/2),grad,1)
    res = cv2.warpAffine(img,M,(cols,rows))
    cv2.imshow('myimg',res)
    loop()

def drehen_rechts():
    global grad
    grad = grad+90
    rows,cols = img.shape[:2]
    M=cv2.getRotationMatrix2D((cols/2,rows/2),grad,1)
    res = cv2.warpAffine(img,M,(cols,rows))
    cv2.imshow('myimg',res)
    loop()

def loop():
    k = cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
    elif k==114:
     drehen_links()
    elif k==105:
        drehen_rechts()
    else:
        cv2.imshow('myimg',img)
        loop()
        
img = cv2.imread("Bilder/ekg.jpg")
cv2.imshow('myimg',img)
loop()
