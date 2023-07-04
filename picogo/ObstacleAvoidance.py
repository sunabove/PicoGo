from machine import Pin, Timer
from time import sleep
import random

from picogo.Robot import Robot
from picogo.UltraSonic import UltraSonic

class ObstacleAvoidance : 

    def __init__( self ):
        self.mode = None
    pass ## __init__

    def run_obstacle_avoidance( self, robot ) :
        duration = 0.1
        
        speed = robot.speed
        max_dist = robot.max_dist
        
        left_block, right_block = robot.read_blocks()
        
        if not left_block and not right_block :
            dist = robot.obstacle_distance()
        else :
            dist = 2*max_dist 
        pass
    
        mode = None
        
        if left_block and right_block :
            mode = robot.right
        elif left_block :   # 좌측 장애물시, 우회전
            mode = robot.right
        elif right_block :  # 우측 장애물시, 좌회전
            mode = robot.left
        elif dist < max_dist : # 전방 장애물 있을 경우, 좌회전 
            mode = robot.left
        else :              # 장매물이 없으면, 전진
            duration = 0 
            mode = robot.forward
        pass
    
        if ( mode is None ) or ( mode is self.mode ) :
            pass
        else :
            if duration :
                robot.stop()
                sleep( duration )
            pass
            
            mode( speed )
        pass
    
        if mode is not None :
            self.mode = mode
        pass

        return left_block, right_block, ( dist < max_dist ) 
    pass ## -- run_ultrasonic_avoidance
    
    def mainImpl( self, robot ) :
        print( f"mainImpl" ) 
        
        left_block = 0
        right_block = 0  
        dist = 0
        
        robot.disp_info_rects()
            
        while robot.run_ext_module :
            duration = robot.duration
            duration = 0 
        
            robot.disp_battery()
            robot.disp_motor() 
        
            [ left_block, right_block, is_obstacle ] = self.run_obstacle_avoidance( robot )
            
            if left_block or right_block or is_obstacle :
                dur_count = random.randint( 30, 50 )
                duration = dur_count*duration
            pass
        
            if duration > 0 :
                sleep( duration )
            pass
        pass

        robot.stop()
        robot.disp_logo()

        print( f"Finished running ultrasonic ir avoidance." )

    pass ## -- mainImpl

pass ## class ObstacleAvoidance

def main( robot ) :
    robot.run_ext_module = True
    
    import _thread
    
    obstacleAvoidance = ObstacleAvoidance()
    
    callback = lambda : obstacleAvoidance.mainImpl( robot=robot )
    
    _thread.start_new_thread( callback, () )
    
    print( "thread inited" )
pass

if __name__ is '__main__' :
    
    print( "Hello ..." )
        
    robot = Robot()
    main( robot )
    
    duration = 30
    print( f"sleep({duration})" )
    sleep( duration )
    print( f"finished sleep({duration})" )
    
    robot.run_ext_module = False
    
    print( "Good bye!" )
    
pass
