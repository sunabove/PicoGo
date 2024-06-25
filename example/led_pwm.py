from picozero import PWMLED
from time import sleep

led = PWMLED(13)

while 1 :
    
    for i in range( 100 ) :
       led.value = i/100
       
       print( "\b"*5, f"{led.value:.2f}", end="" )
       
       sleep( 0.04 )
    pass

pass