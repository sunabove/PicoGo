from time import sleep

from picogo.Robot import Robot
from picogo.UltraSonic import UltraSonic

def main( robot = None ) :
    if robot is None : robot = Robot()
    
    ultraSonic = robot.ultraSonic
    
    duration = 0.02
    speed = 20
    max_dist = 18
    
    obstacle_cnt = 0
    
    while True :
        dist = ultraSonic.distance()
        
        print( f"distance = {dist:6.2f} cm" )
        
        if dist < max_dist :
            obstacle_cnt += 1
            
            if obstacle_cnt == 1 : 
                robot.stop()
                sleep( duration )
            pass
            
            robot.right( 2*speed )
        else:
            ostacle_cnt = 0 
            robot.forward( speed )
        pass
            
        sleep( duration )
    pass 
pass

if __name__ is '__main__' :
    
    print( "Hello ..." )
        
    robot = Robot()
    main( robot )
    
pass
    
    