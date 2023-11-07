from time import sleep
from picozero import Speaker, LED

led = LED(25)
buzzer = Speaker(4)

while 1 :
    led.on()    
    buzzer.on()
    sleep( 2 )
    led.off()
    buzzer.off()
    sleep( 2 )
pass