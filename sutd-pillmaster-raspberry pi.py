import cv2
import numpy as np
from time import sleep
import RPi.GPIO as gpio

arduino = 17 
A = 27
B = 22
gpio.setmode(gpio.BOARD)
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
gpio.setup(arduino,gpio.IN)
gpio.setup(A,gpio.OUT)
gpio.setup(B,gpio.OUT)
while True:
    print("waiting")
    while gpio.input(arduino) == gpio.HIGH:
        gpio.output(A,gpio.LOW)
        gpio.output(B,gpio.LOW)
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
                    gpio.output(A,gpio.HIGH)
                    gpio.output(B,gpio.LOW)
                    #while pin is high sleep
                    if gpio.input(arduino) == gpio.HIGH:
                        while gpio.input(arduino) == gpio.HIGH:
                            sleep(1)
                    else:
                        break
                else:
                    print("extra red")
                    #set the false condition
                    gpio.output(A,gpio.LOW)
                    gpio.output(B,gpio.HIGH)
                    #while pin is high 
                    if gpio.input(arduino) == gpio.HIGH:
                        while gpio.input(arduino) == gpio.HIGH:
                            sleep(1)
                    else:
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
                    gpio.output(A,gpio.HIGH)
                    gpio.output(B,gpio.LOW)
                    #while pin is high sleep
                    if gpio.input(arduino) == gpio.HIGH:
                        while gpio.input(arduino) == gpio.HIGH:
                            sleep(1)
                    else:
                        break
                else:
                    print("extra blue")
                    #set the false condition
                    gpio.output(A,gpio.LOW)
                    gpio.output(B,gpio.HIGH)
                    #while pin is high sleep
                    if gpio.input(arduino) == gpio.HIGH:
                        while gpio.input(arduino) == gpio.HIGH:
                            sleep(1)
                    else:
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
                    gpio.output(A,gpio.HIGH)
                    gpio.output(B,gpio.LOW)
                    #while pin is high sleep
                    if gpio.input(arduino) == gpio.HIGH:
                        while gpio.input(arduino) == gpio.HIGH:
                            sleep(1)
                    else:
                        break
                else:
                    print("extra green")
                    #set the false condition
                    gpio.output(A,gpio.LOW)
                    gpio.output(B,gpio.HIGH)
                    #while pin is high sleep
                    if gpio.input(arduino) == gpio.HIGH:
                        while gpio.input(arduino) == gpio.HIGH:
                            sleep(1)
                    else:
                        break
                        
        cv2.imshow("frame",frame)
        if cv2.waitKey(1)&0xFF==27:
            break
    cap.release()
    cv2.destroyAllWindows()
    gpio.cleanup()

