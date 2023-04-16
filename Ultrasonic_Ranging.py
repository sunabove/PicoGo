from machine import Pin
from time import sleep, ticks_us

echo = Pin(15, Pin.IN)
trig = Pin(14, Pin.OUT)

trig.value(0)
echo.value(0)

def get_dist():
    trig.value(1)
    sleep( 0.1 )
    trig.value(0)
    
    while(echo.value() == 0):
        pass
    
    ts=ticks_us()
    
    while(echo.value() == 1):
        pass
    
    te=ticks_us()
    
    distance=((te-ts)*0.034)/2
    
    return distance
pass

while True:
    dist = get_dist()
    print( f"Distance:{dist:6.2f} cm" )
    sleep(1)
pass