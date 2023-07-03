from time import sleep

from picogo.Robot import Robot

def mainImpl( robot ) :

    print("TRSensor Test Program ...") 
    
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

    print( "calibratedMin = ", robot.trs.calibratedMin )
    print( "calibratedMax = ", robot.trs.calibratedMax )
    print( "calibrate done!")
    print()
    
    robot.stop() 
    sleep(1)

    integral = 0
    last_proportional = 0
    
    robot.disp_info_rects()

    while robot.run_ext_module :
        speed = robot.speed
        maximum = 20
        
        robot.disp_battery()
        robot.disp_motor()
        
        position, sensors = robot.readLine()
        
        print( "position = ", position, ", Sensors = ", sensors )        
        
        # The "proportional" term should be 0 when we are on the line.
        proportional = position - 2000

        # Compute the derivative (change) and integral (sum) of the position.
        derivative = proportional - last_proportional
        integral += proportional

        # Remember the last position.
        last_proportional = proportional
        
        power_diff = proportional/30  + derivative*2;  

        power_diff = max( -maximum, min( power_diff, maximum ) )
        
        if power_diff < 0 :
            robot.move(maximum + power_diff, maximum)
        else:
            robot.move(maximum, maximum - power_diff)
        pass  
    pass

    robot.stop()
    sleep( 1 )

pass

def main( robot ) :
    robot.run_ext_module = True
    
    import _thread 
    
    callback = lambda : mainImpl( robot=robot )
    
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
