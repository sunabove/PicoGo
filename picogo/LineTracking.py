from time import ticks_ms, time, sleep

from picogo.Robot import Robot 

class LineTracking :
    
    def __init__ ( self ) :
        pass
    pass ## -- __init__

    def calibrate( self, robot ) :
        robot.stop()
        sleep( 1 ) 
        
        speed = 30
        
        for i in range(100) :
            if  25 < i <= 75:
                robot.move( speed, -speed, False )
            else:
                robot.move( -speed, speed, False )
            pass
        
            robot.trs_calibrate()
        pass
    
        robot.stop() 
        sleep(1)
        
        print( "calibratedMin = ", robot.trs.calibratedMin )
        print( "calibratedMax = ", robot.trs.calibratedMax )
        print( "calibrate done!")
        print()
        
    pass
        
    def mainImpl( self, robot ) :

        print("Start Lane Tracking ...") 
        
        self.calibrate( robot )

        robot.disp_info_rects() 

        integral = 0
        last_proportional = 0 
        
        then = ticks_ms()/1000
        
        count = 0
        
        while robot.run_ext_module :
            count += 1
            
            speed = robot.speed
            max_speed = min( 80, robot.speed )
            
            robot.disp_battery()
            robot.disp_motor()
            
            duration = robot.duration
            
            pos, sensors, on_line = robot.readLine()
            
            now = ticks_ms()/1000
            
            elapsed = now - then
            
            print( f"[{count:05d}] now = {now}, then = {then}, elpased = {elapsed}, pos = {pos}, sensors = {sensors}" )
            
         
            # PID algorithm
            dt = elapsed   # average 0.083
            proportional = pos*1000 - 2000
            integral += proportional
            derivative = proportional - last_proportional

            # Remember the last position.
            last_proportional = proportional
            
            speed_diff = proportional*0.03  + derivative*1
            # speed_diff = proportional/30  + derivative*2  

            speed_diff = max( - max_speed, min( speed_diff, max_speed ) )
            
            if speed_diff < 0 :
                robot.move( max_speed + speed_diff, max_speed )
            else:
                robot.move( max_speed, max_speed - speed_diff )
            pass
        
            then = now
        
            ## sleep( duration ) 
        pass ## -- mainImpl

        robot.stop() 
        robot.disp_logo()

        print( f"Finished running lane tracking." )

    pass

pass ## -- class LineTracking

def main( robot ) :
    robot.run_ext_module = True
    
    import _thread
    
    lineTracking = LineTracking()
    
    callback = lambda : lineTracking.mainImpl( robot=robot )
    
    _thread.start_new_thread( callback, () )
    
    print( "thread inited" )
pass

if __name__ is '__main__' :
    
    print( "Hello ..." )
        
    robot = Robot()
    main( robot )
    
    duration = 40
    print( f"sleep({duration})" )
    sleep( duration )
    print( f"finished sleep({duration})" )
    
    robot.run_ext_module = False
    
    print( "Good bye!" )
    
pass
