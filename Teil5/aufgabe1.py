import cv2

width=1
height=1

def increase_size():
    global width
    global height
    width=width*1.1
    height=height*1.1
    resized = cv2.resize(img,None,fx=width,fy=height, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('myimg',resized)
    loop()
    
def decrease_size():
    global width
    global height
    width=width*0.9
    height=height*0.9
    resized = cv2.resize(img,None,fx=width,fy=height, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('myimg',resized)
    loop()   

def loop():
    k = cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
    elif k==43:
        increase_size()
    elif k==45:
        decrease_size()
    else:
        cv2.imshow('myimg',img)
        loop()
        
img = cv2.imread("Bilder/ekg.jpg")
cv2.imshow('myimg',img)
loop()
