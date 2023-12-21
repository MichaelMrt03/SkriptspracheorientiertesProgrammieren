import cv2
img = cv2.imread('Bilder/ekg.jpg')
cv2.imshow('myimage1',img)
res = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation= cv2.INTER_CUBIC)
cv2.imshow('myimage2',res)
cv2.waitKey(0)
cv2.destroyAllWindows()