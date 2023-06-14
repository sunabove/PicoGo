import machine
import ujson, utime

from Robot import Robot

print( "Hello ... Bluetooth!" )

robot = Robot()

battery = robot.battery
temperature = robot.temperature

lcd = robot.lcd 

led = robot.led
led.value(1)

buzzer = robot.buzzer
buzzer.value(0)

rgbLed = robot.rgbLed
rgbLed.pixels_set(0, rgbLed.BLACK)
rgbLed.pixels_set(1, rgbLed.BLACK)
rgbLed.pixels_set(2, rgbLed.BLACK)
rgbLed.pixels_set(3, rgbLed.BLACK)
rgbLed.pixels_show()

motor = robot.motor

uart = machine.UART(0, 115200)     # init with given baudrate

LOW_SPEED    =  30
MEDIUM_SPEED =  50
HIGH_SPEED   =  80

speed = 50
t = 0
count = 0 

print( "Ready to accept!" )

while True:
    s = uart.read()
    
    if s != None :
        ##print( "s = " , s )
        
        try:
            count += 1
            j = ujson.loads(s)
            
            print( "j =" , j )
            
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
    
    if s != None and (utime.ticks_ms() - t) > 3000 :
        t = utime.ticks_ms()
        
        text = f"PicoGo\n{count}"
        
        lcd.disp_full_text( text )
        lcd.show()
    pass

pass