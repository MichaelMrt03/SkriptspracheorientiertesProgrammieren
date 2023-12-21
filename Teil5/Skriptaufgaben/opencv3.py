import cv2
img = cv2.imread('Bilder/Verkehrsschilder.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('myimg',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite('pictur_out2.jpg',img)
    cv2.destroyAllWindows()