from picozero import LED
from time import sleep

led = LED(13)
while True :
   led.on()
   sleep(2)
   led.off()
   sleep(2)