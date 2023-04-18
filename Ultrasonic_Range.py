from machine import Pin
from time import sleep, sleep_us, ticks_us

echo = Pin(15, Pin.IN)
trig = Pin(14, Pin.OUT)

trig.value(0)
echo.value(0)

def get_obstacle_distance():
    trig.value(1)
    sleep_us( 10 )
    trig.value(0)
    
    while echo.value() == 0 :
        pass
    
    then = ticks_us()
    
    while echo.value() == 1 :
        pass
    
    now = ticks_us()
    
    distance= (now - then)*0.017
    
    return distance
pass

if __name__=='__main__':
    while True:
        dist = get_obstacle_distance()
        print( f"Distance:{dist:6.2f} cm" )
        sleep(1)
    pass
pass
