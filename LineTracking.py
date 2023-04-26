from TRSensor import TRSensor
from Motor import PicoGo
from time import sleep
from LCD import LCD

if __name__ == '__main__' :
    
    print("TRSensor Test Program ...")
    
    lcd = LCD() 
    lcd.disp_text( f"LineTracking", 50, 60 )
    
    sleep(3)
    
    robot = PicoGo()
    trs = TRSensor()
    
    for i in range(100) :
        if  25 < i <= 75:
            robot.setMotor( 30, -30, False )
        else:
            robot.setMotor(-30, 30, False )
        pass
    
        trs.calibrate()
    pass

    robot.stop()

    print( "calibratedMin = ", trs.calibratedMin )
    print( "calibratedMax = ", trs.calibratedMax )
    print( "calibrate done!")
    print()
    
    sleep(3)

    numSensors = trs.numSensors
    center_position = trs.center_position()
    
    max_power = 20 

    while True:
        position, sensors = trs.readLine()
        
        print( "position = ", position, ", Sensors = ", sensors )        
        
        pos_diff = position - center_position
        
        lcd.disp_text( f"pos  = {position:4.3f}\ndiff = {pos_diff:6.3f}", 50, 60 )
        
        if abs( pos_diff ) < numSensors/4 :
            robot.forward( max_power )
        elif pos_diff > 0 :
            power = max_power*abs(pos_diff)/center_position
            robot.right( power )
        elif pos_diff < 0 :
            power = max_power*abs(pos_diff)/center_position
            robot.left( power )
        pass        
    pass

pass