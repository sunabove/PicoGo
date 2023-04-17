from Motor import PicoGo
from machine import Pin
from time import sleep

robot = PicoGo()
dsr = Pin(2, Pin.IN)
dsl = Pin(3, Pin.IN)

while True:
    dl_status = dsl.value()
    dr_status = dsr.value()    
    
    print( f"left: {dl_status}, right: {dr_status}" )

    if  (dl_status == 0) and (dr_status == 0) : # 양쪽에 장애물이 있을 때, 좌회전
        robot.left(10)
    elif (dl_status == 0) and (dr_status == 1) : # 좌측 장애물시, 우회전
        robot.right(10)
    elif (dl_status == 1) and (dr_status == 0) :  # 우측 장애물시, 좌회전
        robot.left(10)
    else :  # 장매물이 없으면, 전진
        robot.forward( 20 )
    pass
        
    sleep(0.01)
pass
