if __name__ is '__main__' :
    
    from machine import Pin, Timer
    
    led = Pin(25, Pin.OUT)
    
    timer = Timer() 

    class Blink :
        def __init__( self, max_count = 10 ) :
            self.count = 0
            self.max_count = max_count
            
        def blink( self, timer ):
            self.count += 1
                
            if self.count <= self.max_count :
                print( f"[{self.count}] toggle" )
                led.toggle()
            else :
                print( "timer deinit" )
                timer.deinit()
            pass
        pass
    pass

    blink = Blink()

    timer.init( freq=2, mode=Timer.PERIODIC, callback=blink.blink )
    
pass
