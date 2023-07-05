import machine , ujson, time, math
from machine import Pin, Timer
from time import sleep

from picogo.CurrentTime import curr_time_mili
from picogo.Motor import Motor
from picogo.RGBLed import RGBLed
from picogo.LCD import LCD
from picogo.UltraSonic import UltraSonic
from picogo.IRSensor import IRSensor
from picogo.TRSensor import TRSensor
from picogo.Battery import Battery

print( "Import Robot ..." )

class Robot : 
    
    MIN_SPEED   = min_speed  = 15
    LOW_SPEED   = low_speed  = 30
    MED_SPEED   = med_speed  = 50
    HIGHT_SPEED = high_speed = 80
    
    def __init__(self):
        self.speed = self.low_speed
        
        # paramenter for obstacle avoidance
        self.run_ext_module = False
        self.duration = 0.001
        self.max_dist = 15
        
        # location
        self.x = 0
        self.y = 0
        self.ang_deg = 0
        
        # input devices
        self.ultraSonic = UltraSonic()
        self.irSensor = IRSensor()
        self.trs = TRSensor()
        self.battery = Battery() 
        
        # output devices
        self.rgbLed = RGBLed()
        self.buzzer = machine.Pin(4, Pin.OUT)
        self.led = machine.Pin(25, Pin.OUT)
        self.lcd = LCD()
        self.motor = Motor()
        
        # bluetooth uart        
        self.uart = machine.UART(0, 115200)
        
        self.init_robot()
    pass ## -- __init__

    def init_robot( self ):
        print( "init_robot")
        
        lcd = self.lcd
        
        duration = 1
        
        lcd.disp_logo()
        
        self.ledToggle()        
        
        self.beepOnOff( repeat = 1, period = 1.2 )
        sleep( duration )
        
        lcd.disp_version()        
        sleep( duration )
        
        lcd.disp_logo()        
        sleep( duration )
        
        if False :
            lcd.disp_full_text( "PicoRun\nSkySLAM\nVer 1.0", flush=True )    
            sleep( duration )
        pass
        
        print( "done init robot." )
    pass ## -- init_robot

    def disp_info_rects( self ) :
        print( f"disp_info_rects" )
        
        lcd = self.lcd
        lcd.disp_info_rects()
    pass

    def disp_logo( self, flush=1 ) :
        self.lcd.disp_logo(flush=flush)
    pass

    def disp_battery( self, flush=0 ):
        self.lcd.disp_battery( self.battery, flush=flush )
    pass

    def disp_speeds( self, flush=0 ) :
        self.diso_motor( flush=flush )
    pass

    def disp_motor( self, flush=0 ) :
        self.lcd.disp_motor( self.motor, flush=flush )
    pass 

    def read_blocks(self):
        blocks = self.irSensor.read_blocks()
        
        lcd = self.lcd
        lcd.disp_ir_sensor( blocks, flush=True )
        
        return blocks
    pass

    def trs_calibrate( self ) :
        return self.trs.calibrate()
    pass

    def readLine(self, white_line = 0):
        line = [ position, sensors, on_line ] = self.trs.readLine( white_line = white_line )
        
        lcd = self.lcd
        lcd.disp_tr_sensor( position, sensors, flush=True )
        
        return line
    pass

    def obstacle_distance( self ) :
        dist = self.ultraSonic.obstacle_distance()
        
        lcd = self.lcd
        lcd.disp_ultra_sonic( dist, flush=True )
        
        return dist;
    pass 

    def beepOnOff(self, repeat = 1, period = 0.5, verbose=False ) :
        print( "beepOnOff" )
        
        buzzer = self.buzzer
        
        repeat = max( 1, repeat ) 
    
        class BuzzerOnOff :
            def __init__( self, buzzer, max_count = 10, verbose=False ) :
                self.buzzer = buzzer
                self.count = 0
                self.max_count = max_count
                self.verbose = verbose
            pass
                
            def toggle( self, timer ):
                buzzer = self.buzzer
                
                if self.count < self.max_count :
                    if self.verbose : print( f"[{self.count}] toggle" )
                    
                    buzzer.value( int((self.count + 1)%2) )
                else :
                    if self.verbose : print( "timer deinit" )
                    
                    buzzer.value( 0 )
                    
                    timer.deinit()
                pass
            
                self.count += 1
            pass
        pass

        buzzerOnOff = BuzzerOnOff( buzzer=buzzer, max_count = 2*repeat, verbose=verbose )
        
        timer = Timer()
        
        freq = 1/period
        
        timer.init( freq=freq, mode=Timer.PERIODIC, callback=buzzerOnOff.toggle )
    
        print( "done. beepOnOff" )
    pass ## -- beepOnOff

    def beepOnOffOld(self, repeat = 1, period = 0.5 ) :
        print( "beepOnOff" )
        
        buzzer = self.buzzer
        
        repeat = max( 1, repeat )
        
        for i in range( repeat*2 ) :
            buzzer.value( (i+1) % 2 )
            sleep( period )
        pass
    
        print( "done. beepOnOff" )
    pass ## -- beepOnOff

    def ledToggle(self, repeat = 10, period = 0.5, verbose=False ) :
        print( f"ledToggle( repeat={repeat}, period={period} )" )
        
        led = self.led
        
        class LedBlink :
            def __init__( self, led, max_count = 10, verbose=False ) :
                self.led = led
                self.count = 0
                self.max_count = max_count
                self.verbose = verbose
            pass
                
            def blink( self, timer ):
                if self.count < self.max_count :
                    if self.verbose : print( f"[{self.count}] toggle" )
                    
                    self.led.toggle()
                else :
                    if self.verbose : print( "timer deinit" )
                    
                    timer.deinit()
                pass
            
                self.count += 1
            pass
        pass

        ledBlink = LedBlink( led=led, max_count = 2*repeat, verbose=verbose )
        timer = Timer()
        freq = 1/period
        
        timer.init( freq=freq, mode=Timer.PERIODIC, callback=ledBlink.blink )
    pass # -- ledToggle

    def toggleStop( self ):
        msg = f"Robot: toggleStop()"
        print( msg )
        
        self.x = 0
        self.y = 0
        
        ang_deg = - self.ang_deg
        
        self.stop()
        
        self.addRotation( self.ang_deg )
        
        self.stop()
        
        duration = 0.01
        sleep( duration )
    pass # -- toggleStop

    def addRotation( self, ang_deg ) :
        msg =  f"Robot: addRotation( ang_deg = {ang_deg} )"
        print( msg )
        
        self.rotate( ang_deg )
    pass # -- addRotation

    def rotate( self, ang_deg, speed = None ) :
        if speed is None : speed = self.MIN_SPEED
        
        print( f"Robot: rotate ang_deg = {ang_deg}, speed = {speed}" ); 
        
        duration = abs( ang_deg )/speed*0.144
        
        if duration > 0 :
            dir = 1 if ang_deg > 0 else -1
            self.move( dir*speed, -dir*speed )
            
            sleep( duration )
        pass
    
        self.stop() 
    pass # -- rotate

    def translate( self, x, y, speed = None ) :
        if speed is None : speed = self.MIN_SPEED
        
        if x is None : x = 0
        if y is None : y = 0
        
        dist = math.sqrt( x*x + y*y )
        duration = 1.4*dist/speed
        
        print( f"Robot: translate dist = {dist}, duration = {duration}, speed = {speed}" )
        
        self.forward( speed )
        
        self.x += x
        self.y += y
        
        sleep( duration )
        
        self.stop()
    pass # -- translate

    def moveXY( self, x, y = None ):
        msg = f"Robot: moveXY( x = {x}, y = {y} )"
        print( msg )
        
        self.translate( x, y )
    pass # moveXY

    def locateXY( self, x, y ):
        msg = f"Robot: locateXY( x = {x}, y = {y} )"
        print( msg )
        
        self.forward( )
        
        if x is not None : self.x = x
        if y is not None : self.y = y
        
        sleep( 1 )
        
        self.stop()
    pass # moveXY

    def moveToDirection( self, fx, fy, tx, ty, ang_deg ) :
        msg = f"Robot: moeToDirection( fx = {fx}, fy = {fy}, tx = {tx}, ty = {ty}, ang_deg = {ang_deg}"
        print( msg )
        
        dx = tx - fx
        dy = ty - fx
        
        self.forward()
        
        self.x += dx
        self.y += dy        
        
        sleep(1 )
        
        self.stop()
    pass

    def forward(self, speed=None, verbose=False ):
        if speed is None : speed = Robot.LOW_SPEED
        
        self.motor.forward( speed, verbose )
    pass

    def backward(self, speed=None, verbose=False ):
        if speed is None : speed = Robot.LOW_SPEED
        
        self.motor.backward( speed, verbose )
    pass

    def left(self, speed=None, verbose=False ):
        if speed is None : speed = Robot.LOW_SPEED
        
        self.motor.left( speed, verbose )
    pass

    def right(self, speed=None, verbose=False ):
        if speed is None : speed = Robot.LOW_SPEED
        
        self.motor.right( speed, verbose )
    pass

    def stop(self, verbose=False):
        self.motor.stop( verbose )
    pass

    def move(self, left, right, verbose=False):
        if left is None : left = Robot.LOW_SPEED
        if right is None : right = - left
        
        self.motor.move( left, right, verbose )
    pass

    def set_motor(self, left, right, verbose=False):
        self.motor.set_motor( lef, right, verbose )
    pass

pass ## -- class Robot

def test_rotation( robot ) :
    
    for ang_deg in [ 5, 10, 20, 30, 40, 60, 90 ] :
        tot_angle = 0
        
        while tot_angle < 360 :
            print( f"tot_angle = {tot_angle}" )
            robot.addRotation( ang_deg )
            
            tot_angle += ang_deg
            
            sleep( 0.5 )
        pass

        robot.beepOnOff( repeat = 2, period = 1.2 )
        
        sleep( 3 )
        
    pass

    robot.stop()
pass # -- test_rotation

def test_translation( robot ) :
    
    for i in range( 9 ) :
        dist = i + 1
        
        robot.moveXY( dist )
        
        sleep( 2 )
    pass

    robot.stop()
pass # -- test_translation

def test_robot( robot ) :
    test_rotation( robot )
pass

def main( robot ) :
    test_robot( robot=robot )
pass

if __name__ is '__main__' :
    
    print( "Hello ..." )
        
    robot = Robot()
    main( robot )
    
    duration = 1
    print( f"sleep({duration})" )
    sleep( duration )
    print( f"finished sleep({duration})" )
    
    robot.run_ext_module = False
    
    print( "Good bye!" )
    
pass