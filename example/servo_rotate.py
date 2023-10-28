from picozero import Servo
from time import sleep

servo = Servo(15)

duration = 0.03

for _ in range( 2 ):
    # moving from min to max
    for i in range(0, 100):
        servo.value = i / 100
        print( f"servo value = {servo.value}" )
        sleep( duration )

    # moving from max to min
    for i in range(100, 0, -1):
        servo.value = i / 100
        print( f"servo value = {servo.value}" )
        sleep( duration ) 
pass

if True :
    for i in range(0, 51):
        servo.value = i / 100
        print( f"servo value = {servo.value}" )
        sleep( duration )
