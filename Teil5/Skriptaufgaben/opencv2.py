import cv2
img = cv2.imread('Bilder/geschwindigkeit2.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('myimg',img)
cv2.imwrite('picture_out.jpg',img)
cv2.waitKey(0)
cv2.destroyWindow('myimg')