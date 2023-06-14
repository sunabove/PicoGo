import machine
import ujson, utime

from Motor import Motor
from machine import Pin
from RGBLed import RGBLed
from LCD import LCD

print( "Hello ... Bluetooth!" )

battery = machine.ADC(Pin(26))
temperature = machine.ADC(4)

lcd = LCD()
lcd.fill(0xF232)
lcd.line(2,2,70,2,0xBB56)
lcd.line(70,2,85,17,0xBB56)
lcd.line(85,17,222,17,0xBB56)
lcd.line(222,17,237,32,0xBB56)
lcd.line(2,2,2,118,0xBB56)
lcd.line(2,118,17,132,0xBB56)
lcd.line(17,132,237,132,0xBB56)
lcd.line(237,32,237,132,0xBB56)

lcd.text("Raspberry Pi Pico",90,7,0xFF00)
lcd.text("PicoGo",10,7,0x001F)
lcd.text("SkySLM Coorp.",70,120,0x07E0)
lcd.show()

motor = Motor()
led = machine.Pin(25, Pin.OUT)
led.value(1)

buzzer = machine.Pin(4, Pin.OUT)
buzzer.value(0)

rgbLed = RGBLed()
rgbLed.pixels_set(0, rgbLed.BLACK)
rgbLed.pixels_set(1, rgbLed.BLACK)
rgbLed.pixels_set(2, rgbLed.BLACK)
rgbLed.pixels_set(3, rgbLed.BLACK)
rgbLed.pixels_show()

uart = machine.UART(0, 115200)     # init with given baudrate

LOW_SPEED    =  30
MEDIUM_SPEED =  50
HIGH_SPEED   =  80

speed = 50
t = 0

print( "Ready to accept!" )

while True:
    s = uart.read()
    
    if s != None :
        ##print( "s = " , s )
        
        try:
            j = ujson.loads(s)
            
            print( "j = " , j )
            
            cmd=j.get("Forward")
            if cmd != None:
                if cmd == "Down":
                    motor.forward(speed)
                    uart.write("{\"State\":\"Forward\"}")
                elif cmd == "Up":
                    motor.stop()
                    uart.write("{\"State\":\"Stop\"}")
                    
            cmd = j.get("Backward")
            if cmd != None:
                if cmd == "Down":
                    motor.backward(speed)
                    uart.write("{\"State\":\"Backward\"}")
                elif cmd == "Up":
                    motor.stop()
                    uart.write("{\"State\":\"Stop\"}")
             
            cmd = j.get("Left")
            if cmd != None:
                if cmd == "Down":
                    motor.left(20)
                    uart.write("{\"State\":\"Left\"}")
                elif cmd == "Up":
                    motor.stop()
                    uart.write("{\"State\":\"Stop\"}")
                     
            cmd = j.get("Right")
            if cmd != None:
                if cmd == "Down":
                    motor.right(20)
                    uart.write("{\"State\":\"Right\"}")
                elif cmd == "Up":
                    motor.stop()
                    uart.write("{\"State\":\"Stop\"}")
          
            cmd = j.get("Low")
            if cmd == "Down":
                uart.write("{\"State\":\"Low\"}")
                speed = 30

            cmd = j.get("Medium")
            if cmd == "Down":
                uart.write("{\"State\":\"Medium\"}")
                speed = 50

            cmd = j.get("High")
            if cmd == "Down":
                uart.write("{\"State\":\"High\"}")
                speed = 100
            
            cmd = j.get("BZ")
            if cmd != None:
                if cmd == "on":
                    buzzer.value(1)
                    uart.write("{\"BZ\":\"ON\"}")
                    uart.write("{\"State\":\"BZ:\ON\"}")
                elif cmd == "off":
                    buzzer.value(0)
                    uart.write("{\"BZ\":\"OFF\"}")
                    uart.write("{\"State\":\"BZ:\OFF\"}")
            
            cmd = j.get("LED")
            if cmd != None:
                if cmd == "on":
                    led.value(1)
                    uart.write("{\"LED\":\"ON\"}")
                    uart.write("{\"State\":\"LED:\ON\"}")
                elif cmd == "off":
                    led.value(0)
                    uart.write("{\"LED\":\"OFF\"}")
                    uart.write("{\"State\":\"LED:\OFF\"}")
            
            cmd = j.get("RGB")
            if cmd != None:
                rgb=tuple(eval(cmd))
                rgbLed.pixels_set(0, rgb)
                rgbLed.pixels_set(1, rgb)
                rgbLed.pixels_set(2, rgb)
                rgbLed.pixels_set(3, rgb)
                rgbLed.pixels_show()
                uart.write("{\"State\":\"RGB:\("+cmd+")\"}")
        except:
            #print("err")
            pass
        pass
    pass
    
    if (utime.ticks_ms() - t) > 3000 :
        t = utime.ticks_ms()
        reading = temperature.read_u16() * 3.3 / (65535)
        
        temp = 27 - (reading - 0.706)/0.001721
        v = battery.read_u16()*3.3/65535 * 2
        
        p = (v - 3) * 100 / 1.2        
        p = max( 0, min( p, 100 ) )

        lcd.fill_rect(145,50,50,40,0xF232)
        lcd.text("temperature :  {:5.2f} C".format(temp),30,50,0xFFFF)
        lcd.text("Voltage     :  {:5.2f} V".format(v),30,65,0xFFFF)
        lcd.text("percent     :   {:3.1f} %".format(p),30,80,0xFFFF)
        lcd.show()
    pass

pass


import machine
import ujson, utime

from Motor import Motor
from machine import Pin
from RGBLed import RGBLed
from LCD import LCD

print( "Hello ... Bluetooth!" )

battery = machine.ADC(Pin(26))
temperature = machine.ADC(4)

lcd = LCD()
lcd.fill(0xF232)
lcd.line(2,2,70,2,0xBB56)
lcd.line(70,2,85,17,0xBB56)
lcd.line(85,17,222,17,0xBB56)
lcd.line(222,17,237,32,0xBB56)
lcd.line(2,2,2,118,0xBB56)
lcd.line(2,118,17,132,0xBB56)
lcd.line(17,132,237,132,0xBB56)
lcd.line(237,32,237,132,0xBB56)

lcd.text("Raspberry Pi Pico",90,7,0xFF00)
lcd.text("PicoGo",10,7,0x001F)
lcd.text("SkySLM Coorp.",70,120,0x07E0)
lcd.show()

motor = Motor()
led = machine.Pin(25, Pin.OUT)
led.value(1)

buzzer = machine.Pin(4, Pin.OUT)
buzzer.value(0)

rgbLed = RGBLed()
rgbLed.pixels_set(0, rgbLed.BLACK)
rgbLed.pixels_set(1, rgbLed.BLACK)
rgbLed.pixels_set(2, rgbLed.BLACK)
rgbLed.pixels_set(3, rgbLed.BLACK)
rgbLed.pixels_show()

uart = machine.UART(0, 115200)     # init with given baudrate

LOW_SPEED    =  30
MEDIUM_SPEED =  50
HIGH_SPEED   =  80

speed = 50
t = 0

print( "Ready to accept!" )

while True:
    s = uart.read()
    
    if s != None :
        ##print( "s = " , s )
        
        try:
            j = ujson.loads(s)
            
            print( "j = " , j )
            
            cmd=j.get("Forward")
            if cmd != None:
                if cmd == "Down":
                    motor.forward(speed)
                    uart.write("{\"State\":\"Forward\"}")
                elif cmd == "Up":
                    motor.stop()
                    uart.write("{\"State\":\"Stop\"}")
                    
            cmd = j.get("Backward")
            if cmd != None:
                if cmd == "Down":
                    motor.backward(speed)
                    uart.write("{\"State\":\"Backward\"}")
                elif cmd == "Up":
                    motor.stop()
                    uart.write("{\"State\":\"Stop\"}")
             
            cmd = j.get("Left")
            if cmd != None:
                if cmd == "Down":
                    motor.left(20)
                    uart.write("{\"State\":\"Left\"}")
                elif cmd == "Up":
                    motor.stop()
                    uart.write("{\"State\":\"Stop\"}")
                     
            cmd = j.get("Right")
            if cmd != None:
                if cmd == "Down":
                    motor.right(20)
                    uart.write("{\"State\":\"Right\"}")
                elif cmd == "Up":
                    motor.stop()
                    uart.write("{\"State\":\"Stop\"}")
          
            cmd = j.get("Low")
            if cmd == "Down":
                uart.write("{\"State\":\"Low\"}")
                speed = 30

            cmd = j.get("Medium")
            if cmd == "Down":
                uart.write("{\"State\":\"Medium\"}")
                speed = 50

            cmd = j.get("High")
            if cmd == "Down":
                uart.write("{\"State\":\"High\"}")
                speed = 100
            
            cmd = j.get("BZ")
            if cmd != None:
                if cmd == "on":
                    buzzer.value(1)
                    uart.write("{\"BZ\":\"ON\"}")
                    uart.write("{\"State\":\"BZ:\ON\"}")
                elif cmd == "off":
                    buzzer.value(0)
                    uart.write("{\"BZ\":\"OFF\"}")
                    uart.write("{\"State\":\"BZ:\OFF\"}")
            
            cmd = j.get("LED")
            if cmd != None:
                if cmd == "on":
                    led.value(1)
                    uart.write("{\"LED\":\"ON\"}")
                    uart.write("{\"State\":\"LED:\ON\"}")
                elif cmd == "off":
                    led.value(0)
                    uart.write("{\"LED\":\"OFF\"}")
                    uart.write("{\"State\":\"LED:\OFF\"}")
            
            cmd = j.get("RGB")
            if cmd != None:
                rgb=tuple(eval(cmd))
                rgbLed.pixels_set(0, rgb)
                rgbLed.pixels_set(1, rgb)
                rgbLed.pixels_set(2, rgb)
                rgbLed.pixels_set(3, rgb)
                rgbLed.pixels_show()
                uart.write("{\"State\":\"RGB:\("+cmd+")\"}")
        except:
            #print("err")
            pass
        pass
    pass
    
    if (utime.ticks_ms() - t) > 3000 :
        t = utime.ticks_ms()
        reading = temperature.read_u16() * 3.3 / (65535)
        
        temp = 27 - (reading - 0.706)/0.001721
        v = battery.read_u16()*3.3/65535 * 2
        
        p = (v - 3) * 100 / 1.2        
        p = max( 0, min( p, 100 ) )

        lcd.fill_rect(145,50,50,40,0xF232)
        lcd.text("temperature :  {:5.2f} C".format(temp),30,50,0xFFFF)
        lcd.text("Voltage     :  {:5.2f} V".format(v),30,65,0xFFFF)
        lcd.text("percent     :   {:3.1f} %".format(p),30,80,0xFFFF)
        lcd.show()
    pass

pass