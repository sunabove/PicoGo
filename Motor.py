from machine import Pin, PWM
from time import sleep

class PicoGo(object):
    
    def __init__(self):
        self.PWMA = PWM(Pin(16))
        self.PWMA.freq(1000)
        self.PWMB = PWM(Pin(21))
        self.PWMB.freq(1000)
        
        self.AIN2 = Pin(17, Pin.OUT)
        self.AIN1 = Pin(18, Pin.OUT)
        self.BIN1 = Pin(19, Pin.OUT)
        self.BIN2 = Pin(20, Pin.OUT)        
        
        self.stop_cnt = 0 
        self.stop()
    pass
            
    def forward(self,speed):
        if (speed >= 0) and (speed <= 100) :
            print( f"forward: speed = {speed}" )
            self.PWMA.duty_u16(int(speed*0xFFFF/100))
            self.PWMB.duty_u16(int(speed*0xFFFF/100))
            self.AIN2.value(1)
            self.AIN1.value(0)
            self.BIN2.value(1)
            self.BIN1.value(0)
        pass
    pass
        
    def backward(self,speed):
        if (speed >= 0) and (speed <= 100) :
            print( f"backward: speed = {speed}" )
            self.PWMA.duty_u16(int(speed*0xFFFF/100))
            self.PWMB.duty_u16(int(speed*0xFFFF/100))
            self.AIN2.value(0)
            self.AIN1.value(1)
            self.BIN2.value(0)
            self.BIN1.value(1)

    def left(self,speed):
        if (speed >= 0) and (speed <= 100) :
            print( f"left: speed = {speed}" )
            self.PWMA.duty_u16(int(speed*0xFFFF/100))
            self.PWMB.duty_u16(int(speed*0xFFFF/100))
            self.AIN2.value(0)
            self.AIN1.value(1)
            self.BIN2.value(1)
            self.BIN1.value(0)
        pass
    pass
        
    def right(self,speed):
        if (speed >= 0) and (speed <= 100) :
            print( f"right: speed = {speed}" )
            self.PWMA.duty_u16(int(speed*0xFFFF/100))
            self.PWMB.duty_u16(int(speed*0xFFFF/100))
            self.AIN2.value(1)
            self.AIN1.value(0)
            self.BIN2.value(0)
            self.BIN1.value(1)
        pass
    pass
        
    def stop(self):
        if self.stop_cnt :
            print( f"stop: speed = {0}" )
        self.stop_cnt += 1
        
        self.PWMA.duty_u16(0)
        self.PWMB.duty_u16(0)
        self.AIN2.value(0)
        self.AIN1.value(0)
        self.BIN2.value(0)
        self.BIN1.value(0)
    pass

    def setMotor(self, left, right, verbose=True):
        if verbose:
            print( f"setMotor: left = {left}, right = {right}" )
        pass
        
        if (left >= 0) and (left <= 100) :
            self.AIN1.value(0)
            self.AIN2.value(1)
            self.PWMA.duty_u16(int(left*0xFFFF/100))
        elif (left < 0) and (left >= -100) :
            self.AIN1.value(1)
            self.AIN2.value(0)
            self.PWMA.duty_u16(-int(left*0xFFFF/100))
        if (right >= 0) and (right <= 100) :
            self.BIN2.value(1)
            self.BIN1.value(0)
            self.PWMB.duty_u16(int(right*0xFFFF/100))
        elif (right < 0) and (right >= -100) :
            self.BIN2.value(0)
            self.BIN1.value(1)
            self.PWMB.duty_u16(-int(right*0xFFFF/100))
        pass
    pass

pass