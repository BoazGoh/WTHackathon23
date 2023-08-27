import cv2
import numpy as np
from time import sleep
#import RPi.GPIO as gpio

cap=cv2.VideoCapture(0)
lower_rangeR=np.array([0,100,10])
upper_rangeR=np.array([10,255,255])

lower_rangeB=np.array([100,100,10])
upper_rangeB=np.array([130,255,255])

lower_rangeG=np.array([35,100,10])
upper_rangeG=np.array([75,255,255])
n = 0
nr = 0
nb = 0
ng = 0
ch = 2
x = 1 #sub for when the control pin is high
while True:
    x = 1
    while x == 1:
        ret,frame=cap.read()
        frame=cv2.resize(frame,(640,480))
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #red
        maskr=cv2.inRange(hsv,lower_rangeR,upper_rangeR)
        _,mask1=cv2.threshold(maskr,254,255,cv2.THRESH_BINARY)
        cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        #Blue
        maskb=cv2.inRange(hsv,lower_rangeB,upper_rangeB)
        _,mask2=cv2.threshold(maskb,254,255,cv2.THRESH_BINARY)
        cntsb,_=cv2.findContours(mask2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        #Green
        maskg=cv2.inRange(hsv,lower_rangeG,upper_rangeG)
        _,mask3=cv2.threshold(maskg,254,255,cv2.THRESH_BINARY)
        cntsg,_=cv2.findContours(mask3,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        for c in cnts:
            xr=600
            if cv2.contourArea(c)>xr:
                xr,yr,wr,hr=cv2.boundingRect(c)
                cv2.rectangle(frame,(xr,yr),(xr+wr,yr+hr),(0,255,0),2)
                cv2.putText(frame,("Red"),(xr,yr+hr),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
                if nr < ch:
                    print("red")
                    nr=nr+1
                    print(nr)
                    #set the true condition
                    print("tell arduino to dispense")
                    #while pin is high sleep
                    sleep(5)
                    break
                else:
                    print("extra red")
                    #set the false condition
                    print("send error to arduino")
                    #while pin is high sleep
                    sleep(5)
                    break

        for c in cntsb:
            xb=600
            if cv2.contourArea(c)>xb:
                xb,yb,wb,hb=cv2.boundingRect(c)
                cv2.rectangle(frame,(xb,yb),(xb+wb,yb+hb),(0,255,0),2)
                cv2.putText(frame,("Blue"),(xb,yb+hb),cv2.FONT_HERSHEY_SIMPLEX,0.6,(250,0,0),2)
                if nb < ch:
                    print("blue")
                    nb=nb+1
                    print(nb)
                    #set the true condition
                    print("tell arduino to dispense")
                    #while pin is high sleep
                    sleep(5)
                    break
                else:
                    print("extra blue")
                    #set the false condition
                    print("send error to arduino")
                    #while pin is high sleep
                    sleep(5)
                    break
        for c in cntsg:
            xg=600
            if cv2.contourArea(c)>xg:
                xg,yg,wg,hg=cv2.boundingRect(c)
                cv2.rectangle(frame,(xg,yg),(xg+wg,yg+hg),(0,255,0),2)
                cv2.putText(frame,("Green"),(xg,yg+hg),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
                if ng < ch:
                    print("green")
                    ng=ng+1
                    print(ng)
                    #set the true condition
                    print("tell arduino to dispense")
                    #while pin is high sleep
                    sleep(5)
                    break  
                else:
                    print("extra green")
                    #set the false condition
                    print("send error to arduino")
                    #while pin is high sleep 
                    sleep(5)
                    break   
        cv2.imshow("frame",frame)
        print("num of red = ",nr)
        print("num of blue = ",nb)
        print("num of green = ",ng)
        if cv2.waitKey(1)&0xFF==27:
            break
    cap.release()
    cv2.destroyAllWindows()

