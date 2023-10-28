import time
from machine import Pin

# led instrinsic 
led=Pin(25, Pin.OUT)

print( "Hello..." )

i = 0 
while True :
    print( i ); i+= 1
    led.toggle()
    time.sleep(0.5)
pass

print( "Good bye!" )