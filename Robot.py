import machine
import ujson, utime

from time import sleep

from Motor import Motor
from machine import Pin, Timer
from RGBLed import RGBLed
from LCD import LCD

class Robot :
    
    def __init__(self):
        self.rgbLed = RGBLed()
        
        self.buzzer = machine.Pin(4, Pin.OUT)
        self.led = machine.Pin(25, Pin.OUT)
        
        self.battery = machine.ADC(Pin(26))
        self.temperature = machine.ADC(4)
                
        self.lcd = LCD()
        self.motor = Motor()
        
        self.init_robot()
    pass

    def init_robot( self ):
        print( "Hello ... Robot")
        
        self.beepTimer( repeat=1, period=0.6 )
        
        lcd = self.lcd
        lcd.disp_logo()
        
        sleep( 3 ) 
        
    pass

    def beepOnOff(self, repeat = 1, period = 0.5 ) :
        buzzer = self.buzzer
        
        repeat = max( 1, repeat )
        
        for i in range( repeat*2 ) :
            buzzer.value( (i+1) % 2 )
            sleep( period )
        pass
    pass

    def beepTimer(self, repeat = 1, period=0.5):
        timer = Timer()
        
        callback = lambda repeat, period : self.beepOnOff( repeat, period )
        
        timer.init(freq=period, mode=Timer.ONE_SHOT, callback = callback(repeat, period) )
    pass

pass

if __name__ == '__main__' :
    robot = Robot()
pass