import cv2 as cv
import numpy as np
one=[]
two=[]
at=1
def target(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        one.append((x,y))
    if event == cv.EVENT_LBUTTONUP:
        two.append((x,y))
        x1,y1=one[0]
        x2,y2=two[0]
        roi=newsize[y1:y2,x1:x2]
        cv.imwrite("enemy.png", roi)
        
        print(at)
cv.namedWindow("image")
time=1
cap=cv.VideoCapture("burger.mp4")

cv.setMouseCallback("image",target)
while True:
    if at == 1:
        template=cv.imread("enemy.png")
        at=0
        print("asd")
    h,w,k = template.shape
    ret,frame=cap.read()
    #frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    newsize= cv.resize(frame,(640,480))
    
    templatex=cv.matchTemplate(newsize,template,cv.TM_CCOEFF_NORMED)
    a,b,c,d=cv.minMaxLoc(templatex)
    top_left=d
    bottom_right=(top_left[0]+w,top_left[1]+h)
    cv.rectangle(newsize,top_left, bottom_right, (255,0,0), 1)

    new=newsize[top_left[1]:top_left[1]+h,top_left[0]:top_left[0]+w]
    template=new
    cv.imshow("image",newsize)

    key=cv.waitKey(time)
    if key== ord("q"):
        break
    elif key== ord("w"):
        time=0
    elif key== ord("e"):
        time=1
    elif key== ord("d"):
        time=200
    elif key== ord("r"):
        at=1
        one=[]
        two=[]   
cap.release()
cv.destroyAllWindows()
