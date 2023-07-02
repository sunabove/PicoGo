from time import sleep

from picogo.TRSensor import TRSensor
from picogo.Motor import Motor
from picogo.LCD import LCD

if __name__ == '__main__' :
    
    print("TRSensor Test Program ...")
    
    lcd = LCD() 
    lcd.disp_text( f"LineTracking", 50, 60 )
    
    motor = Motor()
    trs = TRSensor()
    
    motor.stop()
    
    sleep(3)
    
    for i in range(100) :
        if  25 < i <= 75:
            motor.set_motor( 30, -30, False )
        else:
            motor.set_motor( -30, 30, False )
        pass
    
        trs.calibrate()
    pass

    motor.stop()

    print( "calibratedMin = ", trs.calibratedMin )
    print( "calibratedMax = ", trs.calibratedMax )
    print( "calibrate done!")
    print()
    
    sleep(3)

    numSensors = trs.numSensors
    center_position = trs.center_position()
    
    max_power = 15 

    while True:
        position, sensors = trs.readLine()
        
        print( "position = ", position, ", Sensors = ", sensors )        
        
        pos_diff = position - center_position
        
        lcd.disp_text( f"pos  = {position:4.3f}\ndiff = {pos_diff:6.3f}", 50, 60 )
        
        if True :
            power_diff = max_power*pos_diff/center_position
            
            motor.move( max_power + power_diff, max_power - power_diff )
        elif abs( pos_diff ) < numSensors/4 :
            motor.forward( max_power )
        elif pos_diff > 0 :
            power = max_power*abs(pos_diff)/center_position
            
            motor.right( power )
        elif pos_diff < 0 :
            power = max_power*abs(pos_diff)/center_position
            
            motor.left( power )
        pass
    
        sleep( 0.1 )
    pass

pass