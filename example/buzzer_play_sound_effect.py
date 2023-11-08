from time import sleep
from picozero import Speaker, LED
from random import randint

led = LED(25)

speaker = Speaker(4)

def win():
    for i in range(2000, 5000, 100):
        speaker.play(i, 0.05)
    pass
pass

def bird_chirp():
    for _ in range(2):
        for i in range(5000, 2999, -100):
            speaker.play(i, 0.02)
        sleep(0.2)
    pass
pass
        
for i in range( 10 ):
    led.on()
    win()
    sleep(2)
    
    led.off()
    bird_chirp()
    sleep(2)
pass

led.off()