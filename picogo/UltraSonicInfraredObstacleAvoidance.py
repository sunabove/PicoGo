from machine import Pin
from time import sleep

from picogo.Robot import Robot
from picogo.UltraSonic import UltraSonic 

def main( robot = None ) :
    if robot is None : robot = Robot()
    
    robot.run_ext_module = True
    
    motor = robot.motor
    
    ultraSonic = robot.ultraSonic
    irSensor = robot.irSensor
    
    duration = 0.01
    speed = robot.low_speed
    max_dist = 18
    
    left_block = False
    right_block = False  
    dist = 0
        
    while robot.run_ext_module :
        
        left_block, right_block = irSensor.read_blocks()
        
        if not left_block and not right_block :
            dist = ultraSonic.distance()
        else :
            dist = 2*max_dist 
        pass
        
        if left_block and right_block :
            motor.backward( speed )
        elif left_block :   # 좌측 장애물시, 우회전
            motor.right( speed ) 
        elif right_block :  # 우측 장애물시, 좌회전
            motor.left( speed ) 
        elif dist < max_dist : # 전방 장애물 있을 경우, 좌회전 
            motor.left( speed ) 
        else :              # 장매물이 없으면, 전진
            motor.forward( speed ) 
        pass
    
        if left_block or right_block or dist < max_dist :
            sleep( 5*duration )
        else :
            sleep( duration )
        pass
    
    pass

    print( f"Finished running ultrasonic ir avoidance." )

pass ## -- main

if __name__ is '__main__' :
    
    print( "Hello ..." )
        
    robot = Robot()
    main( robot )
    
pass
