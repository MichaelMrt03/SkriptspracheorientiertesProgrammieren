import cv2
import numpy as np


def loop():
    k = cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
    elif k==49:#1
        #hist
    elif k==50:#2
        #hist
    else:
        cv2.imshow('myimg',img)
        loop()
        
img = cv2.imread("Bilder/ekg.jpg")
cv2.imshow('myimg',img)
loop()
