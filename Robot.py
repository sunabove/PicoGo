import machine
import ujson, utime

from time import sleep

from Motor import Motor
from machine import Pin
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
        lcd = self.lcd
        lcd.disp_logo()
        
        sleep( 3 )
    pass

pass