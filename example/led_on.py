from picozero import LED
from time import sleep

led = LED(25)

led.on()

sleep( 1 )

led.off()