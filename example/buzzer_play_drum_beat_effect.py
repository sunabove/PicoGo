from time import sleep
from picozero import Speaker, LED
from random import randint

led = LED(25)

speaker = Speaker(4) 

for i in range(100):
    led.toggle()
    speaker.play(randint(500, 5000), duration=1)
    sleep(0.001)
    speaker.off()
    sleep(0.5)
pass

led.off()