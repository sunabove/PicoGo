from picozero import LED
from time import sleep

led = LED(25)

while 1 :
   led.toggle()
   print( led.value )
   sleep(1)
pass