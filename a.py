import cv2
import numpy as np
import requests
from datetime import datetime
from pytz import timezone
import time


cap = cv2.VideoCapture(0)

ROOM02_Checker = None
ROOM03_Checker = None
ROOM04_Checker = None
ROOM05_Checker = None
ROOM06_Checker = None
ROOM07_Checker = None
ROOM08_Checker = None
ROOM09_Checker = None
ROOM10_Checker = None

hav_room_01 = ""
hav_room_02 = ""
hav_room_03 = ""
hav_room_04 = ""
hav_room_05 = ""
hav_room_06 = ""
hav_room_07 = ""
hav_room_08 = ""
hav_room_09 = ""
hav_room_10 = ""
value01 = "ROOM01 : Closed\n"
value02 = "";
value03 = "";
value04 = "";
value05 = "";
value06 = "";
value07 = "";
value08 = "";
value09 = "";
value10 = "ROOM10 : Closed\n"
value01_ = "";
value02_ = "";
value03_ = "";
value04_ = "";
value05_ = "";
value06_ = "";
value07_ = "";
value08_ = "";
value09_ = "";
value10_ = "";

img_G = cv2.imread("/home/pi/a/img/Green.jpg")
img_R = cv2.imread("/home/pi/a/img/Red.jpg")

Y_Refresh_Time_ = datetime.now(timezone('Asia/Bangkok'))
Y_Date_ = Y_Refresh_Time_.strftime("%d/%m/%Y")


def msg_line(msg):
    url = 'https://notify-api.line.me/api/notify'
    token = 'Vz7K8UEqnRMYyZSMAfGjEk0DLlS4SLmvOIx7VS9Ai9p'
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
    r = requests.post(url, headers=headers , data = {'message':msg})
    time.sleep(2)

def refresh_time():
    global Refresh_Time,Date_,Hour_,Min_,Sec_,Hour_Count
    Refresh_Time = datetime.now(timezone('Asia/Bangkok'))
    Date_ = Refresh_Time.strftime("%d/%m/%Y")
    Hour_ = Refresh_Time.strftime("%H")
    Min_ = Refresh_Time.strftime("%M")
    Sec_ = Refresh_Time.strftime("%S")
    Hour_Count = Refresh_Time.strftime("%H.%M")
    
    #Link function alert
    check_color()
    alert_time()

def alert_time():
    global value01,value02,value03,value04,value05,value06,value07,value08,value09,value10
    global value01_,value02_,value03_,value04_,value05_,value06_,value07_,value08_,value09_,value10_
    global hav_room_01,hav_room_02,hav_room_03,hav_room_04,hav_room_05,hav_room_06,hav_room_07,hav_room_08,hav_room_09,hav_room_10
    global Y_Date_,Y_Refresh_Time_

    if Min_ == "00" and Sec_ <= "15":
        msg_line("\n\nวันที่ : "+Date_+"\nเวลา : "+Hour_Count+" น.\n\n"+value01+value02+value03+value04+value05+value06+value07+value08+value09+value10+"\nห้องที่มีแขกเข้าพัก\nวันที่ : "+Y_Date_+"\n"+hav_room_01+hav_room_02+hav_room_03+hav_room_04+hav_room_05+hav_room_06+hav_room_07+hav_room_08+hav_room_09+hav_room_10)
        time.sleep(20)
        
    if Hour_ == "08" and Min_ == "30" and Sec_ <= "15":
        msg_line("\n\nห้องที่มีแขกเข้าพัก\nวันที่ "+Y_Date_+"\n\n"+hav_room_01+hav_room_02+hav_room_03+hav_room_04+hav_room_05+hav_room_06+hav_room_07+hav_room_08+hav_room_09+hav_room_10+"\n\nhttps://docs.google.com/spreadsheets/d/1kjx1V7whCfeQI8LNxCOEDPzAFPsZqR4qtKkToQn_9G8\n")
        
        #Google sheert
        url = "http://api.pushingbox.com/pushingbox?devid=v0829FE9ACAAF3D0&value1="+value01_+"&value2="+value02_+"&value3="+value03_+"&value4="+value04_+"&value5="+value05_+"&value6="+value06_+"&value7="+value07_+"&value8="+value08_+"&value9="+value09_+"&value10="+value10_
        r = requests.get(url)
        
        time.sleep(20)
    
    if Hour_ == "12" and Min_ == "30" and Sec_ <= "15":        

        if ROOM02_Checker == True:
            hav_room_02 = "ROOM02\n"
            value02_ = "Done";
        elif ROOM02_Checker == False:
            hav_room_02 = ""
            value02_ = "";

        if ROOM03_Checker == True:
            hav_room_03 = "ROOM03\n"
            value03_ = "Done";
        elif ROOM03_Checker == False:
            hav_room_03 = ""
            value03_ = "";
            
        if ROOM04_Checker == True:
            hav_room_04 = "ROOM04\n"
            value04_ = "Done";
        elif ROOM04_Checker == False:
            hav_room_04 = ""
            value04_ = "";
            
        if ROOM05_Checker == True:
            hav_room_05 = "ROOM05\n"
            value05_ = "Done";
        elif ROOM05_Checker == False:
            hav_room_05 = ""
            value05_ = "";
            
        if ROOM06_Checker == True:
            hav_room_06 = "ROOM06\n"
            value06_ = "Done";
        elif ROOM06_Checker == False:
            hav_room_06 = ""
            value06_ = "";
            
        if ROOM07_Checker == True:
            hav_room_07 = "ROOM07\n"
            value07_ = "Done";
        elif ROOM07_Checker == False:
            hav_room_07 = ""
            value07_ = "";
            
        if ROOM08_Checker == True:
            hav_room_08 = "ROOM08\n"
            value08_ = "Done";
        elif ROOM08_Checker == False:
            hav_room_08 = ""
            value08_ = "";
            
        if ROOM09_Checker == True:
            hav_room_09 = "ROOM09\n"
            value09_ = "Done";
        elif ROOM09_Checker == False:
            hav_room_09 = ""
            value09_ = "";
            
#        if ROOM10_Checker == True:
#            hav_room_10 = "ROOM10\n"
#            value10_ = "Done";
#        elif ROOM010Checker == False:
#            hav_room_10 = ""
#            value10_ = "";

         #refresh time result room
        Y_Refresh_Time_ = datetime.now(timezone('Asia/Bangkok'))
        Y_Date_ = Y_Refresh_Time_.strftime("%d/%m/%Y")
        time.sleep(20)

    ### 13 AM.
    if Hour_ == "13" and Min_ == "30" and Sec_ <= "15":        
        
        if ROOM02_Checker == True:
            hav_room_02 = "ROOM02\n"
            value02_ = "Done";
        elif ROOM02_Checker == False:
            hav_room_02 = ""
            value02_ = "";

        if ROOM03_Checker == True:
            hav_room_03 = "ROOM03\n"
            value03_ = "Done";
        elif ROOM03_Checker == False:
            hav_room_03 = ""
            value03_ = "";
            
        if ROOM04_Checker == True:
            hav_room_04 = "ROOM04\n"
            value04_ = "Done";
        elif ROOM04_Checker == False:
            hav_room_04 = ""
            value04_ = "";
            
        if ROOM05_Checker == True:
            hav_room_05 = "ROOM05\n"
            value05_ = "Done";
        elif ROOM05_Checker == False:
            hav_room_05 = ""
            value05_ = "";
            
        if ROOM06_Checker == True:
            hav_room_06 = "ROOM06\n"
            value06_ = "Done";
        elif ROOM06_Checker == False:
            hav_room_06 = ""
            value06_ = "";
            
        if ROOM07_Checker == True:
            hav_room_07 = "ROOM07\n"
            value07_ = "Done";
        elif ROOM07_Checker == False:
            hav_room_07 = ""
            value07_ = "";
            
        if ROOM08_Checker == True:
            hav_room_08 = "ROOM08\n"
            value08_ = "Done";
        elif ROOM08_Checker == False:
            hav_room_08 = ""
            value08_ = "";
            
        if ROOM09_Checker == True:
            hav_room_09 = "ROOM09\n"
            value09_ = "Done";
        elif ROOM09_Checker == False:
            hav_room_09 = ""
            value09_ = "";
            
#        if ROOM10_Checker == True:
#            hav_room_10 = "ROOM10\n"
#            value10_ = "Done";
#        elif ROOM010Checker == False:
#            hav_room_10 = ""
#            value10_ = ""
        
        time.sleep(20)
        
        
def check_color():
#    global G_g2,G_g3,G_g4,G_g5,G_g6,G_g7,G_g8,G_g9,G_g10,G_b2,G_b3,G_b4,G_b5,G_b6,G_b7,G_b8,G_b9,G_b10,G_r2,G_r3,G_r4,G_r5,G_r6,G_r7,G_r8,G_r9,G_r10
    global R_g2,R_g3,R_g4,R_g5,R_g6,R_g7,R_g8,R_g9,R_g10,R_b2,R_b3,R_b4,R_b5,R_b6,R_b7,R_b8,R_b9,R_b10,R_r2,R_r3,R_r4,R_r5,R_r6,R_r7,R_r8,R_r9,R_r10

    ret, frame = cap.read()
    hsv_green = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # Crop Size & Position LED
    Crop_ROOM02 = hsv_green[250:255,40:45]
    Crop_ROOM03 = hsv_green[240:245,100:105]
    Crop_ROOM04 = hsv_green[235:240,170:175]
    Crop_ROOM05 = hsv_green[230:235,245:250]
    Crop_ROOM06 = hsv_green[220:225,320:325]
    Crop_ROOM07 = hsv_green[210:215,385:390]
    Crop_ROOM08 = hsv_green[210:215,465:470]
    Crop_ROOM09 = hsv_green[200:205,530:535]
    Crop_ROOM10 = hsv_green[185:190,600:605]
#
#    Differnce_G_02 = cv2.subtract(img_G,Crop_ROOM02)
#    Differnce_G_03 = cv2.subtract(img_G,Crop_ROOM03)
#    Differnce_G_04 = cv2.subtract(img_G,Crop_ROOM04)
#    Differnce_G_05 = cv2.subtract(img_G,Crop_ROOM05)
#    Differnce_G_06 = cv2.subtract(img_G,Crop_ROOM06)
#    Differnce_G_07 = cv2.subtract(img_G,Crop_ROOM07)
#    Differnce_G_08 = cv2.subtract(img_G,Crop_ROOM08)
#    Differnce_G_09 = cv2.subtract(img_G,Crop_ROOM09)
#    Differnce_G_10 = cv2.subtract(img_G,Crop_ROOM10)
#    
    Differnce_R_02 = cv2.subtract(img_R,Crop_ROOM02)
    Differnce_R_03 = cv2.subtract(img_R,Crop_ROOM03)
    Differnce_R_04 = cv2.subtract(img_R,Crop_ROOM04)
    Differnce_R_05 = cv2.subtract(img_R,Crop_ROOM05)
    Differnce_R_06 = cv2.subtract(img_R,Crop_ROOM06)
    Differnce_R_07 = cv2.subtract(img_R,Crop_ROOM07)
    Differnce_R_08 = cv2.subtract(img_R,Crop_ROOM08)
    Differnce_R_09 = cv2.subtract(img_R,Crop_ROOM09)
    Differnce_R_10 = cv2.subtract(img_R,Crop_ROOM10)
#
#    G_b2, G_g2, G_r2 = cv2.split(Differnce_G_02)
#    G_b3, G_g3, G_r3 = cv2.split(Differnce_G_03)
#    G_b4, G_g4, G_r4 = cv2.split(Differnce_G_04)
#    G_b5, G_g5, G_r5 = cv2.split(Differnce_G_05)
#    G_b6, G_g6, G_r6 = cv2.split(Differnce_G_06)
#    G_b7, G_g7, G_r7 = cv2.split(Differnce_G_07)
#    G_b8, G_g8, G_r8 = cv2.split(Differnce_G_08)
#    G_b9, G_g9, G_r9 = cv2.split(Differnce_G_09)
#    G_b10, G_g10, G_r10 = cv2.split(Differnce_G_10)   
#    
    R_b2, R_g2, R_r2 = cv2.split(Differnce_R_02)
    R_b3, R_g3, R_r3 = cv2.split(Differnce_R_03)
    R_b4, R_g4, R_r4 = cv2.split(Differnce_R_04)
    R_b5, R_g5, R_r5 = cv2.split(Differnce_R_05)
    R_b6, R_g6, R_r6 = cv2.split(Differnce_R_06)
    R_b7, R_g7, R_r7 = cv2.split(Differnce_R_07)
    R_b8, R_g8, R_r8 = cv2.split(Differnce_R_08)
    R_b9, R_g9, R_r9 = cv2.split(Differnce_R_09)
    R_b10, R_g10, R_r10 = cv2.split(Differnce_R_10)
    

while(True):

    refresh_time()
    

    
#    #Check Green scale
#    print("ROOM 02 Blue : ",cv2.countNonZero(G_b2),"  Green : ",cv2.countNonZero(G_g2),"  Red : ",cv2.countNonZero(G_r2))
#    print("ROOM 03 Blue : ",cv2.countNonZero(G_b3),"  Green : ",cv2.countNonZero(G_g3),"  Red : ",cv2.countNonZero(G_r3))
#    print("ROOM 04 Blue : ",cv2.countNonZero(G_b4),"  Green : ",cv2.countNonZero(G_g4),"  Red : ",cv2.countNonZero(G_r4))
#    print("ROOM 05 Blue : ",cv2.countNonZero(G_b5),"  Green : ",cv2.countNonZero(G_g5),"  Red : ",cv2.countNonZero(G_r5))
#    print("ROOM 06 Blue : ",cv2.countNonZero(G_b6),"  Green : ",cv2.countNonZero(G_g6),"  Red : ",cv2.countNonZero(G_r6))
#    print("ROOM 07 Blue : ",cv2.countNonZero(G_b7),"  Green : ",cv2.countNonZero(G_g7),"  Red : ",cv2.countNonZero(G_r7))
#    print("ROOM 08 Blue : ",cv2.countNonZero(G_b8),"  Green : ",cv2.countNonZero(G_g8),"  Red : ",cv2.countNonZero(G_r8))
#    print("ROOM 09 Blue : ",cv2.countNonZero(G_b9),"  Green : ",cv2.countNonZero(G_g9),"  Red : ",cv2.countNonZero(G_r9))
#    print("ROOM 10 Blue : ",cv2.countNonZero(G_b10),"  Green : ",cv2.countNonZero(G_g10),"  Red : ",cv2.countNonZero(G_r10),"\n\n")
#    
#    print("ROOM 02 Blue : ",cv2.countNonZero(R_b2),"  Green : ",cv2.countNonZero(R_g2),"  Red : ",cv2.countNonZero(R_r2))
#    print("ROOM 03 Blue : ",cv2.countNonZero(R_b3),"  Green : ",cv2.countNonZero(R_g3),"  Red : ",cv2.countNonZero(R_r3))
#    print("ROOM 04 Blue : ",cv2.countNonZero(R_b4),"  Green : ",cv2.countNonZero(R_g4),"  Red : ",cv2.countNonZero(R_r4))
#    print("ROOM 05 Blue : ",cv2.countNonZero(R_b5),"  Green : ",cv2.countNonZero(R_g5),"  Red : ",cv2.countNonZero(R_r5))
#    print("ROOM 06 Blue : ",cv2.countNonZero(R_b6),"  Green : ",cv2.countNonZero(R_g6),"  Red : ",cv2.countNonZero(R_r6))
#    print("ROOM 07 Blue : ",cv2.countNonZero(R_b7),"  Green : ",cv2.countNonZero(R_g7),"  Red : ",cv2.countNonZero(R_r7))
#    print("ROOM 08 Blue : ",cv2.countNonZero(R_b8),"  Green : ",cv2.countNonZero(R_g8),"  Red : ",cv2.countNonZero(R_r8))
#    print("ROOM 09 Blue : ",cv2.countNonZero(R_b9),"  Green : ",cv2.countNonZero(R_g9),"  Red : ",cv2.countNonZero(R_r9))
#    print("ROOM 10 Blue : ",cv2.countNonZero(R_b10),"  Green : ",cv2.countNonZero(R_g10),"  Red : ",cv2.countNonZero(R_r10),"\n\n")
#    
#    time.sleep(1)
    
    
    
    # Condition Check ROOM02

    if cv2.countNonZero(R_r2) == 0 and ROOM02_Checker != True:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r2) == 0 and ROOM02_Checker != True:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r2) == 0 and ROOM02_Checker != True:
                ROOM02_Checker = True
                print("ROOM02 Check-ON !")
                msg_line("ROOM02 Check-ON !")
                value02 = "ROOM02 : ON !\n"
                hav_room_02 = "ROOM02\n"
                value02_ = "Done"
                
                
    if cv2.countNonZero(R_r2) == 25 and ROOM02_Checker != False:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r2) == 25 and ROOM02_Checker != False:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r2) == 25 and ROOM02_Checker != False:
                ROOM02_Checker = False
                print("ROOM02 Check-OFF")
                msg_line("ROOM02 Check-OFF")
                
                #Time check-out
                Refresh_T02 = datetime.now(timezone('Asia/Bangkok')) 
                value02 = "ROOM02 : OFF " + Refresh_T02.strftime("%d/%m - %H:%M\n")

 
     # Condition Check ROOM03

    if cv2.countNonZero(R_r3) == 0 and ROOM03_Checker != True:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r3) == 0 and ROOM03_Checker != True:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r3) == 0 and ROOM03_Checker != True:
                ROOM03_Checker = True
                print("ROOM03 Check-ON !")
                msg_line("ROOM03 Check-ON !")
                value03 = "ROOM03 : ON !\n"
                hav_room_03 = "ROOM03\n"
                value03_ = "Done"
 
                
    if cv2.countNonZero(R_r3) == 25 and ROOM03_Checker != False:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r3) == 25 and ROOM03_Checker != False:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r3) == 25 and ROOM03_Checker != False:
                ROOM03_Checker = False
                print("ROOM03 Check-OFF")
                msg_line("ROOM03 Check-OFF")
                
                #Time check-out
                Refresh_T03 = datetime.now(timezone('Asia/Bangkok')) 
                value03 = "ROOM03 : OFF " + Refresh_T03.strftime("%d/%m - %H:%M\n")

                
    # Condition Check ROOM04

    if cv2.countNonZero(R_r4) == 0 and ROOM04_Checker != True:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r4) == 0 and ROOM04_Checker != True:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r4) == 0 and ROOM04_Checker != True:
                ROOM04_Checker = True
                print("ROOM04 Check-ON !")
                msg_line("ROOM04 Check-ON !")
                value04 = "ROOM04 : ON !\n"
                hav_room_04 = "ROOM04\n"
                value04_ = "Done"
                
                
    if cv2.countNonZero(R_r4) == 25 and ROOM04_Checker != False:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r4) == 25 and ROOM04_Checker != False:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r4) == 25 and ROOM04_Checker != False:
                ROOM04_Checker = False
                print("ROOM04 Check-OFF")
                msg_line("ROOM04 Check-OFF")
                
                #Time check-out
                Refresh_T04 = datetime.now(timezone('Asia/Bangkok')) 
                value04 = "ROOM04 : OFF " + Refresh_T04.strftime("%d/%m - %H:%M\n")
                
                
    # Condition Check ROOM05

    if cv2.countNonZero(R_r5) == 0 and ROOM05_Checker != True:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r5) == 0 and ROOM05_Checker != True:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r5) == 0 and ROOM05_Checker != True:
                ROOM05_Checker = True
                print("ROOM05 Check-ON !")
                msg_line("ROOM05 Check-ON !")
                value05 = "ROOM05 : ON !\n"
                hav_room_05 = "ROOM05\n"
                value05_ = "Done"
                
                
    if cv2.countNonZero(R_r5) == 25 and ROOM05_Checker != False:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r5) == 25 and ROOM05_Checker != False:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r5) == 25 and ROOM05_Checker != False:
                ROOM05_Checker = False
                print("ROOM05 Check-OFF")
                msg_line("ROOM05 Check-OFF")
                
                #Time check-out
                Refresh_T05 = datetime.now(timezone('Asia/Bangkok')) 
                value05 = "ROOM05 : OFF " + Refresh_T05.strftime("%d/%m - %H:%M\n")
                
                
    # Condition Check ROOM06

    if cv2.countNonZero(R_r6) == 0 and ROOM06_Checker != True:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r6) == 0 and ROOM06_Checker != True:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r6) == 0 and ROOM06_Checker != True:
                ROOM06_Checker = True
                print("ROOM06 Check-ON !")
                msg_line("ROOM06 Check-ON !")
                value06 = "ROOM06 : ON !\n"
                hav_room_06 = "ROOM06\n"
                value06_ = "Done"
                
                
    if cv2.countNonZero(R_r6) == 25 and ROOM06_Checker != False:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r6) == 25 and ROOM06_Checker != False:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r6) == 25 and ROOM06_Checker != False:
                ROOM06_Checker = False
                print("ROOM06 Check-OFF")
                msg_line("ROOM06 Check-OFF")
                
                #Time check-out
                Refresh_T06 = datetime.now(timezone('Asia/Bangkok')) 
                value06 = "ROOM06 : OFF " + Refresh_T06.strftime("%d/%m - %H:%M\n")
                
                
    # Condition Check ROOM07

    if cv2.countNonZero(R_r7) == 0 and ROOM07_Checker != True:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r7) == 0 and ROOM07_Checker != True:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r7) == 0 and ROOM07_Checker != True:
                ROOM07_Checker = True
                print("ROOM07 Check-ON !")
                msg_line("ROOM07 Check-ON !")
                value07 = "ROOM07 : ON !\n"
                hav_room_07 = "ROOM07\n"
                value07_ = "Done"
                
                
    if cv2.countNonZero(R_r7) == 25 and ROOM07_Checker != False:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r7) == 25 and ROOM07_Checker != False:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r7) == 25 and ROOM07_Checker != False:
                ROOM07_Checker = False
                print("ROOM07 Check-OFF")
                msg_line("ROOM07 Check-OFF")
                
                #Time check-out
                Refresh_T07 = datetime.now(timezone('Asia/Bangkok')) 
                value07 = "ROOM07 : OFF " + Refresh_T07.strftime("%d/%m - %H:%M\n")
                
                
    # Condition Check ROOM08

    if cv2.countNonZero(R_r8) == 0 and ROOM08_Checker != True:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r8) == 0 and ROOM08_Checker != True:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r8) == 0 and ROOM08_Checker != True:
                ROOM08_Checker = True
                print("ROOM08 Check-ON !")
                msg_line("ROOM08 Check-ON !")
                value08 = "ROOM08 : ON !\n"
                hav_room_08 = "ROOM08\n"
                value08_ = "Done"
                
                
    if cv2.countNonZero(R_r8) == 25 and ROOM08_Checker != False:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r8) == 25 and ROOM08_Checker != False:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r8) == 25 and ROOM08_Checker != False:
                ROOM08_Checker = False
                print("ROOM08 Check-OFF")
                msg_line("ROOM08 Check-OFF")
                
                #Time check-out
                Refresh_T08 = datetime.now(timezone('Asia/Bangkok')) 
                value08 = "ROOM08 : OFF " + Refresh_T08.strftime("%d/%m - %H:%M\n")
                
                
    # Condition Check ROOM09

    if cv2.countNonZero(R_r9) == 0 and ROOM09_Checker != True:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r9) == 0 and ROOM09_Checker != True:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r9) == 0 and ROOM09_Checker != True:
                ROOM09_Checker = True
                print("ROOM09 Check-ON !")
                msg_line("ROOM09 Check-ON !")
                value09 = "ROOM09 : ON !\n"
                hav_room_09 = "ROOM09\n"
                value09_ = "Done"
                
                
    if cv2.countNonZero(R_r9) == 25 and ROOM09_Checker != False:
        time.sleep(5)
        refresh_time()
        
        if cv2.countNonZero(R_r9) == 25 and ROOM09_Checker != False:
            time.sleep(5)
            refresh_time()
            
            if cv2.countNonZero(R_r9) == 25 and ROOM09_Checker != False:
                ROOM09_Checker = False
                print("ROOM09 Check-OFF")
                msg_line("ROOM09 Check-OFF")
                
                #Time check-out
                Refresh_T09 = datetime.now(timezone('Asia/Bangkok')) 
                value09 = "ROOM09 : OFF " + Refresh_T09.strftime("%d/%m - %H:%M\n")
                
                
#    # Condition Check ROOM10
#
#    if cv2.countNonZero(R_r10) == 0 and ROOM10_Checker != True:
#        time.sleep(5)
#        refresh_time()
#        
#        if cv2.countNonZero(R_r10) == 0 and ROOM10_Checker != True:
#            time.sleep(5)
#            refresh_time()
#            
#            if cv2.countNonZero(R_r10) == 0 and ROOM10_Checker != True:
#                ROOM10_Checker = True
#                print("ROOM10 Check-ON !")
#                msg_line("ROOM10 Check-ON !")
#                value10 = "ROOM10 : ON !\n"
#                hav_room_10 = "ROOM10\n"
#                value10_ = "Done"
#                
#
#    if cv2.countNonZero(R_r10) == 25 and ROOM10_Checker != False:
#        time.sleep(5)
#        refresh_time()
#        
#        if cv2.countNonZero(R_r10) == 25 and ROOM10_Checker != False:
#            time.sleep(5)
#            refresh_time()
#            
#            if cv2.countNonZero(R_r10) == 25 and ROOM10_Checker != False:
#                ROOM10_Checker = False
#                print("ROOM10 Check-OFF")
#                msg_line("ROOM10 Check-OFF")
#                
#                #Time check-out
#                Refresh_T10 = datetime.now(timezone('Asia/Bangkok')) 
#                value10 = "ROOM10 : OFF " + Refresh_T10.strftime("%d/%m - %H:%M\n")
#                
#


    
# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()

