import machine
import ujson, utime

from Robot import Robot

class BlueTooth :
    def __init__( self ):
        print( "Hello ... Bluetooth!" )
        
        self.robot = Robot()
        
        self.init_bluetooth()
    pass

    def init_bluetooth( self ) :
        robot = self.robot
        
        rgbLed = robot.rgbLed
        rgbLed.pixels_set(0, rgbLed.BLACK)
        rgbLed.pixels_set(1, rgbLed.BLACK)
        rgbLed.pixels_set(2, rgbLed.BLACK)
        rgbLed.pixels_set(3, rgbLed.BLACK)
        rgbLed.pixels_show()
                
    pass

    def process_json_cmd( self, s, robot ) :
        try :
            self.process_json_cmd_impl( s, robot )
        except Exception as e :
            print( e ) 
        pass
    pass
    
    def process_json_cmd_impl( self, json, robot ) :
        uart = robot.uart
        
        motor = robot.motor
        rgbLed = robot.rgbLed
        buzzer = robot.buzzer
        led = robot.led
        
        speed = robot.speed
        
        cmd = json.get("Forward")
        
        print( f"cmd = {cmd}" )
        
        if cmd != None:
            if cmd == "Down":
                motor.forward(speed, verbose=True)
                uart.write("{\"State\":\"Forward\"}")
            elif cmd == "Up":
                motor.stop()
                uart.write("{\"State\":\"Stop\"}")
                
        cmd = json.get("Backward")
        if cmd != None:
            if cmd == "Down":
                motor.backward(speed)
                uart.write("{\"State\":\"Backward\"}")
            elif cmd == "Up":
                motor.stop()
                uart.write("{\"State\":\"Stop\"}")
         
        cmd = json.get("Left")
        if cmd != None:
            if cmd == "Down":
                motor.left(20)
                uart.write("{\"State\":\"Left\"}")
            elif cmd == "Up":
                motor.stop()
                uart.write("{\"State\":\"Stop\"}")
                 
        cmd = json.get("Right")
        if cmd != None:
            if cmd == "Down":
                motor.right(20)
                uart.write("{\"State\":\"Right\"}")
            elif cmd == "Up":
                motor.stop()
                uart.write("{\"State\":\"Stop\"}")
      
        cmd = json.get("Low")
        if cmd == "Down":
            uart.write("{\"State\":\"Low\"}")
            robot.speed = robot.low_speed

        cmd = json.get("Medium")
        if cmd == "Down":
            uart.write("{\"State\":\"Medium\"}")
            robot.speed = robot.med_speed

        cmd = json.get("High")
        if cmd == "Down":
            uart.write("{\"State\":\"High\"}")
            robot.speed = robot.high_speed
        
        cmd = json.get("BZ")
        if cmd != None:
            if cmd == "on":
                buzzer.value(1)
                uart.write("{\"BZ\":\"ON\"}")
                uart.write("{\"State\":\"BZ:\ON\"}")
            elif cmd == "off":
                buzzer.value(0)
                uart.write("{\"BZ\":\"OFF\"}")
                uart.write("{\"State\":\"BZ:\OFF\"}")
        
        cmd = json.get("LED")
        if cmd != None:
            if cmd == "on":
                led.value(1)
                uart.write("{\"LED\":\"ON\"}")
                uart.write("{\"State\":\"LED:\ON\"}")
            elif cmd == "off":
                led.value(0)
                uart.write("{\"LED\":\"OFF\"}")
                uart.write("{\"State\":\"LED:\OFF\"}")
        
        cmd = json.get("RGB")
        if cmd != None:
            rgb = tuple( eval(cmd) )
            
            rgbLed.pixels_set(0, rgb)
            rgbLed.pixels_set(1, rgb)
            rgbLed.pixels_set(2, rgb)
            rgbLed.pixels_set(3, rgb)
            
            rgbLed.pixels_show()
            
            uart.write("{\"State\":\"RGB:\("+cmd+")\"}")
        pass
    pass

    def read_bytes( self, uart, nbytes ) :
        byte_list = bytearray( nbytes )
            
        i = 0 
        while i < nbytes : 
            b = uart.read( 1 )
            if b :
                byte_list[ i ] = b[0]
                i += 1
            pass
        pass

        return byte_list
    pass

    def main( self ) :
        print( "Ready to accept!" )
        
        t = 0
        count = 0 

        robot = self.robot

        uart = robot.uart

        head_read_count = 0
        
        while True :
            debug = False
            
            data_type = 0
            data_len  = 0
            
            while data_type == 0 :
                head_read_count += 1
                # read start of heading
                b = self.read_bytes( uart, 1 )    
                b = b[0]
                
                debug and print( f"[{head_read_count:04d}] start of heading = {b}" )
                
                if b != 1 :
                    data_type = 0
                    data_len  = 0
                elif b == 1 : # Start of Heading
                    # read data type
                    b = self.read_bytes( uart, 1 )
                    data_type = b[0] 
                    
                    # read data_len
                    if data_type : 
                        byte_list = self.read_bytes( uart, 2 )
                        
                        data_len = 0
                        for b in byte_list :
                            data_len = data_len*255 + b
                        pass
                    pass
                pass
            pass

            print( f"date_type = {data_type}, data_len = {data_len}" )

            # reate data
            data = None
            
            if data_len > 0 :
                data = self.read_bytes( uart, data_len )  
            pass

            # read end of transmission
            if True : 
                byte_list = self.read_bytes( uart, 1 )  
            
                if byte_list[0] != 4 : # End of Transmission
                    data = None
                pass
            pass

            if data : 
                s = data.decode()
            pass
            
            if s != None :
                print( f"s = {s}" )
                count += 1
                
                if s == "display pair code" :
                    pair_code = robot.lcd.disp_pairing_code( flush=True )
                    
                    uart.write( f"pair code: {pair_code}" )
                else :
                    json = None
                    
                    try : 
                        json = ujson.loads(s)
                    except Exception as e:
                        #print( e )
                        pass
                    pass
        
                    if json != None :
                        print( "json =" , json )
        
                        self.process_json_cmd( json, robot )
                    pass
                pass
            pass
            
            if s != None and (utime.ticks_ms() - t) > 3000 :
                t = utime.ticks_ms()
                
                text = f"PicoGo\n{count}"
                
                robot.lcd.disp_full_text( text )
                robot.lcd.show()
            pass

        pass
    pass

pass

def main() :
    blueTooth = BlueTooth()
    blueTooth.main()
pass

if __name__ == '__main__' :
    main()
pass
    