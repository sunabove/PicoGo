import utime
from machine import Pin
from Motor import PicoGo

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

while True:
    dist = get_obstacle_distance()
    dr_status = dsr.value()
    dl_status = dsl.value()
    if (dist <= 20) or (dl_status == 0) or (dr_status == 0) :
        robot.right(20)
    else:
        robot.forward(25)
        
    utime.sleep_ms(20)
pass