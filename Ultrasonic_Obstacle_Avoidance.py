from time import sleep, sleep_us, ticks_us
from machine import Pin
from Motor import PicoGo
from Ultrasonic_Range import get_obstacle_distance

robot = PicoGo()

if __name__ == '__main__' :
    print( "Hello" )

    start = ticks_us()   
    duration = 0.1
    
    obstacle_cnt = 0 
    while True :
        dist = get_obstacle_distance()
        
        print( f"distance: {dist:6.2f} cm" )
        
        if dist < 20 :
            if obstacle_cnt : 
                robot.stop()
                sleep( duration )
            
            ostacle_cnt += 1
            
            robot.right(20)
            sleep( duration )
        else:
            ostacle_cnt = 0 
            robot.forward(20)
        pass
            
        sleep( duration )
        
        now = ticks_us()
        elapsed = now - start
        
        print( f"start = {start:,}, now = {now:,}, duration = {elapsed:,}" ) 
        
        if elapsed > 60*10**6 : break
    pass

    robot.stop()

    print( "Good bye!" )
pass