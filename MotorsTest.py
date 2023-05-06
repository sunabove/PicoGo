from Motors import Motors
from time import sleep 

if __name__== '__main__' :
    motors = Motors()
    
    duration = 1
    
    motors.forward(50)
    sleep(duration)
    motors.backward(50)
    sleep(duration)
    motors.left(30)
    sleep(duration)
    motors.right(30)
    sleep(duration)
    motors.stop()
pass