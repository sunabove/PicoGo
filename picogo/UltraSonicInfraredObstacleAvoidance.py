from machine import Pin
from time import sleep
import random

from picogo.Robot import Robot
from picogo.UltraSonic import UltraSonic 

def main( robot = None ) :
    if robot is None : robot = Robot()
    
    robot.run_ext_module = True
    
    left_block = 0
    right_block = 0  
    dist = 0
    
    robot.disp_info_rects()
        
    while robot.run_ext_module :
        duration = robot.duration
        speed = robot.speed
        max_dist = robot.max_dist
        
        robot.disp_battery()
        robot.disp_motor()
        
        left_block, right_block = robot.read_blocks()
        
        if not left_block and not right_block :
            dist = robot.obstacle_distance()
        else :
            dist = 2*max_dist 
        pass
        
        if left_block and right_block :
            robot.backward( speed )
        elif left_block :   # 좌측 장애물시, 우회전
            robot.right( speed ) 
        elif right_block :  # 우측 장애물시, 좌회전
            robot.left( speed ) 
        elif dist < max_dist : # 전방 장애물 있을 경우, 좌회전 
            robot.left( speed ) 
        else :              # 장매물이 없으면, 전진
            robot.forward( speed ) 
        pass
    
        if left_block or right_block or dist < max_dist :
            dur_count = random.randint( 30, 50 )
            sleep( dur_count*duration )
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
