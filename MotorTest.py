from Motor import PicoGo
from time import sleep 

if __name__== '__main__' :
    robot = PicoGo()
    
    duration = 1
    
    robot.forward(50)
    sleep(duration)
    robot.backward(50)
    sleep(duration)
    robot.left(30)
    sleep(duration)
    robot.right(30)
    sleep(duration)
    robot.stop()
pass