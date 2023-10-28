from time import sleep
from machine import Pin, PWM

pwm = PWM(Pin(15))
pwm.freq(50)
duration = 0.02

for _ in range( 2 ) :
    for position in range(1000, 9000 + 50, 50):
        print( f"position = {position}" )
        pwm.duty_u16(position)
        sleep( duration )
        
    for position in range(9000, 1000 - 50, -50):
        print( f"position = {position}" )
        pwm.duty_u16(position)
        sleep( duration )
pass

for position in range(1000, 5000 + 50, 50):
    print( f"position = {position}" )
    pwm.duty_u16(position)
    sleep( duration )

print( "Good bye!" )
