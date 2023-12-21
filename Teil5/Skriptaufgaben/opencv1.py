import cv2

img = cv2.imread('Bilder/ekg.jpg',cv2.IMREAD_COLOR)
cv2.imshow('myimg',img)
cv2.waitKey(0)
cv2.destroyWindow('myimg')