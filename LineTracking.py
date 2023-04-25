from TRSensor import TRSensor
from Motor import PicoGo
from time import sleep

if __name__ == '__main__' :
    print("TRSensor Test Program ...")
    sleep(3)
    robot = PicoGo()

    trs = TRSensor()
    for i in range(100):
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
    
    sleep(5)

    numSensors = trs.numSensors
    center_position = trs.center_position()
    
    maximum = 20
    integral = 0
    last_proportional = 0

    while True:
        position, sensors = trs.readLine()
        
        print( "position = ", position, ", Sensors = ", sensors )        
        
        diff = position - center_position
        power_diff = maximum*diff/center_position
        
        robot.setMotor(maximum + power_diff, maximum - power_diff)

    pass

pass