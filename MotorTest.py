from Motor import Motor
from time import sleep 

if __name__== '__main__' :
    motor = Motor()
    
    duration = 1
    
    motor.forward(50)
    sleep(duration)
    
    motor.backward(50)
    sleep(duration)
    
    motor.left(30)
    sleep(duration)
    
    motor.right(30)
    sleep(duration)
    
    motor.stop()
    sleep(duration)
pass