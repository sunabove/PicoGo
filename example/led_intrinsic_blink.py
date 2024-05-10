import time
from machine import Pin

# led instrinsic 
led=Pin(25, Pin.OUT)

print( "Hello..." )

while 1 :
    led.toggle()
    time.sleep(0.5)
pass

print( "Good bye!" )