from machine import Pin
from Motor import PicoGo
from time import sleep, sleep_ms
import machine 
import rp2

@rp2.asm_pio(out_shiftdir=0, autopull=True, pull_thresh=12, autopush=True, push_thresh=12, sideset_init=(rp2.PIO.OUT_LOW), out_init=rp2.PIO.OUT_LOW)
def spi_cpha0():
    out(pins, 1).side(0x0)[1]
    in_(pins, 1).side(0x1)[1]
pass
        
class TRSensor():
    
    def __init__(self):
        self.numSensors = 5
        
        self.calibratedMin = [0] * self.numSensors
        self.calibratedMax = [1023] * self.numSensors
        
        self.last_position = 0
        self.Clock     = 6
        self.Address   = 7
        self.DataOut   = 27
        self.CS        = Pin(28, Pin.OUT)
        self.CS.value(1)
        self.sm = rp2.StateMachine(1, spi_cpha0, freq=800_000, sideset_base=Pin(self.Clock, Pin.OUT), out_base=Pin(self.Address, Pin.OUT), in_base=Pin(self.DataOut, Pin.IN))
        self.sm.active(1)
    pass

    def center_position(self) :
        return self.numSensors/2 - 0.5
    pass
        
    """
    Reads the sensor values into an array. There *MUST* be space
    for as many values as there were sensors specified in the constructor.
    Example usage:
    unsigned int sensor_values[8];9
    sensors.read(sensor_values);
    The values returned are a measure of the reflectance in abstract units,
    with higher values corresponding to lower reflectance (e.g. a black
    surface or a void).
    """     
    def readAnalog(self):
        value = [0]*( self.numSensors + 1 )
        
        #Read Channel~channe5 AD value
        for j in range( self.numSensors+1 ):
            self.CS.value(0)
            #set channe
            self.sm.put(j << 28)
            #get last channe value
            value[j] = self.sm.get() & 0xfff
            self.CS.value(1)
            value[j] >>= 2
        pass
    
        sleep_ms(2)
        
        return value[1:]
    pass
    
    """
    Reads the sensors 10 times and uses the results for
    calibration.  The sensor values are not returned; instead, the
    maximum and minimum values found over time are stored internally
    and used for the readCalibrated() method.
    """
    def calibrate(self):
        numSensors = self.numSensors
        max_sensor_values = [0]*numSensors
        min_sensor_values = [0]*numSensors
        
        for j in range(10):        
            sensor_values = self.readAnalog();
            
            for i in range(numSensors):            
                # set the max we found THIS time
                if (j == 0) or max_sensor_values[i] < sensor_values[i] :
                    max_sensor_values[i] = sensor_values[i]
                pass

                # set the min we found THIS time
                if (j == 0) or min_sensor_values[i] > sensor_values[i] :
                    min_sensor_values[i] = sensor_values[i]
                pass
            pass
        
        pass

        # record the min and max calibration values
        for i in range(numSensors):
            if min_sensor_values[i] > self.calibratedMin[i] :
                self.calibratedMin[i] = min_sensor_values[i]
            pass
        
            if max_sensor_values[i] < self.calibratedMax[i] :
                self.calibratedMax[i] = max_sensor_values[i]
            pass
        pass
    
    pass
        
    """
    Returns values calibrated to a value between 0 and 1000, where
    0 corresponds to the minimum value read by calibrate() and 1000
    corresponds to the maximum value.  Calibration values are
    stored separately for each sensor, so that differences in the
    sensors are accounted for automatically.
    
    """  
    def readCalibrated(self):
        value = 0
        sensor_values = self.readAnalog()
        
        for i in range (0,self.numSensors):
            denominator = self.calibratedMax[i] - self.calibratedMin[i]

            if(denominator != 0):
                value = (sensor_values[i] - self.calibratedMin[i])* 1000 / denominator

            if(value < 0):
                value = 0
            elif(value > 1000):
                value = 1000

            sensor_values[i] = int(value)

        return sensor_values
    pass

    """
    Operates the same as read calibrated, but also returns an
    estimated position of the robot with respect to a line.
    The estimate is made using a weighted average of the sensor indices
    multiplied by 1000, so that a return value of 0 indicates that
    the line is directly below sensor 0,
    a return value of 1000 indicates that the line is directly below sensor 1,
    2000 indicates that it's below sensor 2, etc.
    Intermediate values indicate that the line is between two sensors.
    
    The formula is:

         0*value0 + 1000*value1 + 2000*value2 + ...
       -----------------------------------------------
             value0  +  value1  +  value2 + ...

    By default, this function assumes a dark line (high values)
    surrounded by white (low values).
    If your line is light on black, set the optional second argument white_line to true.
    In this case, each sensor value will be replaced by (1000-value) before the averaging.
    """
    def readLine(self, white_line = 0):
        sensor_values = self.readCalibrated()
        
        numSensors = self.numSensors
        
        weighted_total = 0
        total_value = 0
        on_line = 0        
        
        for i, value in enumerate( sensor_values ):             
            if white_line :
                value = 1_000 - value
            pass
            
            # keep track of whether we see the line at all
            if value > 200 :
                on_line = 1
            pass
                
            # only average in values that are above a noise threshold
            if value > 50 :
                weighted_total += value*(i+1)    # this is for the weighted total,
                total_value += value                # this is for the denominator
            pass
        pass

        if not on_line :
            # If it last read to the left of center, return 0.
            if self.last_position < numSensors/2 :
                #print("left")
                self.last_position = 0
            else: # If it last read to the right of center, return the max.
                #print("right")
                self.last_position = numSensors - 1
        else:
            self.last_position = weighted_total/total_value - 1
        pass

        return self.last_position, sensor_values
    pass

pass

if __name__ == '__main__':
    
    from LCD import LCD
    
    print( "TRSensor Test ... \n" )
    
    lcd = LCD() 
    lcd.disp_text( f"PicoGo by SkySLAM", 50, 60 ) 
    
    trs = TRSensor()
    
    print( "center position = ", trs.center_position() )
    
    if True :
        sleep(3)
        
        lcd.disp_text( f"Calibrating ....", 50, 60 )
        
        robot = PicoGo()
        
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
        print( "calibrate done! \n" )
        
        lcd.disp_text( f"Calibrating done!", 50, 60 )
    else :
        trs.calibrate()
    pass
    
    idx = 0 
    while True:
        idx += 1
        if True :
            position, sensors = trs.readLine()
            print( f"[{idx:4d}] position = {position:+.2f}, sensors = {sensors}" )
            
            lcd.disp_text( f"[{idx:4d}] position = {position:.2f}", 10, 15, LCD.WHITE )
        else : 
            #digits = trs.readAnalog()
            digits = trs.readCalibrated()
            
            avg = sum( digits ) / len( digits )
            
            print( "avg: = ", avg, " ", digits )
        pass
    
        sleep( 1 )
    pass

pass 