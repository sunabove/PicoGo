from picozero import LED
from time import sleep

led = LED(13)

while 1 :
   led.toggle()
   print( "\b"*4, led.value, end="" )
   sleep(1)
pass