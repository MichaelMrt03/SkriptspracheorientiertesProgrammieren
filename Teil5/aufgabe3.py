import cv2
import numpy as np
from matplotlib import pyplot as plt

def graustufenhistogramm():
    plt.hist(img.ravel(),256,[0,256])
    plt.show()

def farbhistogramm():
     color = ('b','g','r')
     for i,col in enumerate(color):
         histr = cv2.calcHist([img],[i],None,[256],[0,256])
         plt.plot(histr,color=col)
         plt.xlim([0,256])
         plt.show()

def loop():
    k = cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
    elif k==49:#1
        graustufenhistogramm()
    elif k==50:#2
        farbhistogramm()
    else:
        cv2.imshow('myimg',img)
        loop()
        
img = cv2.imread("Bilder/geschwindigkeit2.jpg")
cv2.imshow('myimg',img)
loop()
