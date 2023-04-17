from machine import Pin
from Motor import PicoGo
import utime
from time import sleep

robot = PicoGo()
dsr = Pin(2, Pin.IN)
dsl = Pin(3, Pin.IN)

echo = Pin(15, Pin.IN)
trig = Pin(14, Pin.OUT)
trig.value(0)
echo.value(0)

def get_obstacle_distance():
    trig.value(1)
    utime.sleep_us(10)
    trig.value(0)
    while echo.value() == 0:
        pass
    ts=utime.ticks_us()
    while echo.value() == 1:
        pass
    te=utime.ticks_us()
    distance=((te-ts)*0.034)/2
    
    return distance
pass

speed = 30
    
while True:
    dist = get_obstacle_distance()
    dr_status = dsr.value()
    dl_status = dsl.value()
    
    if (dl_status == 0) and (dr_status == 0) : # 양쪽에 장애물이 있을 때, 좌회전
        robot.left( speed/2 )
    elif (dl_status == 0) and (dr_status == 1) : # 좌측 장애물시, 우회전
        robot.right( speed/2 )
    elif (dl_status == 1) and (dr_status == 0) :  # 우측 장애물시, 좌회전
        robot.left( speed/2 )
    elif dist < 20 :
        robot.right( speed/2 )    
    else :  # 장매물이 없으면, 전진
        robot.forward( speed )
    pass
        
    sleep( 0.1 )
pass