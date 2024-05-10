from picozero import LED
from time import sleep

led = LED(13)

while 1 :
   led.toggle()
   sleep(1)
pass