from machine import Pin, SPI
from time import sleep
from Battery import Battery
from UltraSonic import UltraSonic

import framebuf
import builtins

# ST7789
class LCD(framebuf.FrameBuffer):
    
    # RGC 565 Color Definition
    WHITE  = 0xFFFF
    BLACK  = 0x0000
    GREEN  = 0x001F
    RED    = 0x00F0
    BLUE   = 0xFF00
    GBLUE  = 0X07FF
    YELLOW = 0xF0FF
    
    def __init__(self):
        self.width = 240
        self.height = 135
        
        self.bg = self.BLACK  # background color
        self.fg = self.WHITE  # foreground color
        
        self.texts = []
        self.text_idx = 0 
        
        self.inited_print = False
        
        self.rst = Pin(12,Pin.OUT)
        self.bl = Pin(13,Pin.OUT)
        self.bl(1)
        
        self.cs = Pin(9,Pin.OUT)
        self.cs(1)
        self.spi = SPI(1)
        self.spi = SPI(1,1000_000)
        self.spi = SPI(1,10000_000,polarity=0, phase=0,sck=Pin(10),mosi=Pin(11),miso=None)
        self.dc = Pin(8,Pin.OUT)
        self.dc(1)
        self.buffer = bytearray(self.height * self.width * 2)
        
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.init_display()
        
        self.fill( self.bg ) 
        
        x = 0
        y = 0
        rc = row_count = 6
        
        width = self.width
        height = self.height
        
        self.rect( x, y, width, height - 1, self.fg, False )
        
        m = 4
        
        rects = self.rects = []
        
        x = m
        w = width - 2*m
        h = int( (height - (rc + 2)*m - 1)/rc )
        
        for idx in range( rc ) :
            y = idx*h + (idx + 1)*m
            rect = [ x, y, w, h, m ]
            rects.append( rect )
        pass
        
        for r in rects :
            self.rect( r[0], r[1], r[2], r[3], self.fg, False )
        pass
    
    pass
        
    def write_cmd(self, cmd):
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)
    pass

    def write_data(self, buf):
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(bytearray([buf]))
        self.cs(1)
    pass

    def init_display(self):
        """Initialize dispaly"""
        self.rst(1)
        self.rst(0)
        self.rst(1)
        
        self.write_cmd(0x36)
        self.write_data(0x70)

        self.write_cmd(0x3A) 
        self.write_data(0x05)

        self.write_cmd(0xB2)
        self.write_data(0x0C)
        self.write_data(0x0C)
        self.write_data(0x00)
        self.write_data(0x33)
        self.write_data(0x33)

        self.write_cmd(0xB7)
        self.write_data(0x35) 

        self.write_cmd(0xBB)
        self.write_data(0x19)

        self.write_cmd(0xC0)
        self.write_data(0x2C)

        self.write_cmd(0xC2)
        self.write_data(0x01)

        self.write_cmd(0xC3)
        self.write_data(0x12)   

        self.write_cmd(0xC4)
        self.write_data(0x20)

        self.write_cmd(0xC6)
        self.write_data(0x0F) 

        self.write_cmd(0xD0)
        self.write_data(0xA4)
        self.write_data(0xA1)

        self.write_cmd(0xE0)
        self.write_data(0xD0)
        self.write_data(0x04)
        self.write_data(0x0D)
        self.write_data(0x11)
        self.write_data(0x13)
        self.write_data(0x2B)
        self.write_data(0x3F)
        self.write_data(0x54)
        self.write_data(0x4C)
        self.write_data(0x18)
        self.write_data(0x0D)
        self.write_data(0x0B)
        self.write_data(0x1F)
        self.write_data(0x23)

        self.write_cmd(0xE1)
        self.write_data(0xD0)
        self.write_data(0x04)
        self.write_data(0x0C)
        self.write_data(0x11)
        self.write_data(0x13)
        self.write_data(0x2C)
        self.write_data(0x3F)
        self.write_data(0x44)
        self.write_data(0x51)
        self.write_data(0x2F)
        self.write_data(0x1F)
        self.write_data(0x1F)
        self.write_data(0x20)
        self.write_data(0x23)
        
        self.write_cmd(0x21)
        self.write_cmd(0x11)
        self.write_cmd(0x29)
    pass

    def show(self):
        self.write_cmd(0x2A)
        self.write_data(0x00)
        self.write_data(0x28)
        self.write_data(0x01)
        self.write_data(0x17)
        
        self.write_cmd(0x2B)
        self.write_data(0x00)
        self.write_data(0x35)
        self.write_data(0x00)
        self.write_data(0xBB)
        
        self.write_cmd(0x2C)
        
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(self.buffer)
        self.cs(1)
    pass

    def disp_text(self, text, x, y, fg=None, bg=None, show=True) :
        if bg is None : bg = self.bg
        if fg is None : fg = self.fg
        
        width = self.width
        height = self.height
        
        self.rect( 2, 2, width -5, height -5, bg, True )
        
        for t in text.split( "\n" ) : 
            self.text( t, x, y, fg )
            y += 15
        pass
    
        show and self.show()
    pass # disp_text

    def print(self, *args, **kwargs) :
        width = self.width; height = self.height
        line_height = 15
        
        x = 0 ; y = 0
        
        m = 4
        w = width - 1
        h = int( (height - m - 1)/2 )
        y = h + m
        
        self.rect( x, y, w, h, self.bg, True )
        self.rect( x, y, w, h, self.fg, False )
        
        fg = None
        if "c" in kwargs :
            fg = kwargs.pop( "c" )
        elif "fg" in kwargs :
            fg = kwargs.pop( "fg" )
        else :
            fg = self.fg
        pass
    
        texts = "".join( args )
        
        for text in texts.split( "\n" ) :
            self.texts.append( [ text, fg, self.text_idx ] )
            self.text_idx += 1
        pass
    
        while len( self.texts ) > 8 :
            self.texts.pop( 0 )
        pass
    
        x = 10
        y += line_height 
        
        line_count = int( (height - y)/line_height )
        
        #print( f"line count = {line_count}" )
        
        for text in self.texts[ - line_count :  ] :
            t = text[ 0 ]
            fg = text[ 1 ]
            text_idx = text[ 2 ]
            
            t = f"[{text_idx + 1:2d}] {t}"
            self.text( t, x, y, fg )
            y += line_height
            
            #builtins.print( text )
        pass
        
        if False :
            builtins.print( "LCD : ", end="" )
            builtins.print( *args, **kwargs )
        pass
    pass # print

    def disp_init( self ) :
        self.disp_battery()
        self.disp_ultra_sonic()
    pass

    def disp_battery( self, values = [0, 0, 0], verbose=False ) : # 배터리 잔량 표시 
        
        if isinstance( values , Battery ) :
            values = values.read()
        pass 
        
        temp, voltage, percent = values
        
        color = LCD.GREEN
        if percent < 33 :
            color = LCD.RED
        elif percent < 66 :
            color = LCD.BLUE
        else :
            color = LCD.GREEN
        pass
    
        fg = self.fg
        
        x, y, w, h, m = self.rects[0]
        
        self.rect( x, y, w, h, LCD.GBLUE, True )
        self.rect( x, y, int( w*percent/100 ), h, color, True )
        self.rect( x, y, w, h, fg, False )
        
        self.text( f"{int(percent):3d} %", int(x + w/2 - 25), int( y + 5), LCD.WHITE )
        
        verbose and print( f"Temperature = {temp:.3f} °C, Voltage = {voltage:.3f} V, Percent = {percent:.2} %" )
        
    pass # disp_battery

    def disp_ultra_sonic( self, dist = 0 ) :  # 초음파 센서 거리 표시 
        
        if isinstance( dist, UltraSonic ) :
            dist = dist.get_obstacle_distance()
        pass 
        
        color = LCD.GREEN
        
        max_dist = 40
        
        if dist <= 10 :
            color = 0xFFF0            
        elif dist <= 20 :
            color = LCD.RED
        elif dist <= 30 :
            color = LCD.BLUE
        else :
            color = LCD.GREEN
        pass
    
        fg = self.fg
        bg = self.bg
        
        x, y, w, h, m = self.rects[1]
        
        value_width = int( w*min(max_dist, dist)/max_dist )
        
        self.rect( x, y, w, h, LCD.GBLUE, True )
        
        if False :
            self.rect( x, y, value_width, h, color, True )
        else :
            cw = cell_width = int(w/10)
            
            for idx in range( int(value_width/cw + 0.5) ):
                c = color
                self.rect( x + idx*cw, y, cw - m, h, c, True )
            pass
        pass
        
        self.rect( x, y, w, h, fg, False )
        
        #self.text( f"{dist: 6.2f} cm", int(x + w/2 - 30), int( y + 5), LCD.WHITE )
    
    pass # disp_ultra_sonic

pass

if __name__== '__main__' :
    # print ultra sonic
    
    lcd = LCD()
    ultraSonic = UltraSonic()
    
    lcd.disp_init()
    
    while 1 :
        dist = ultraSonic.obstacle_distance()
        lcd.disp_ultra_sonic( dist )
        lcd.show()
        
        print( f"Distance = {dist:6.2f} cm" )
        sleep( 0.1)
    pass
elif __name__== '__main__' :
    # lcd battery print
    
    lcd = LCD()    
    battery = Battery()
    
    idx = 0
    from random import randint
    while True :
        idx += 1
        
        values = [ temp, voltage, percent ] = battery.read()
        
        #values = [ temp,  voltage, randint( 0, 100 ) ] 
        
        lcd.disp_battery( values, 1 )
        lcd.show()
        
        sleep( 1 )
    pass 
elif __name__== '__main__' :    
    lcd = LCD()
    lcd.show()
elif __name__== '__main__ 2' :
    # LCDPrintTest.py
    
    lcd = LCD() 
    
    lcd.print( "Hello...." )
    lcd.print( "Raspberry Pi Pico", c=LCD.BLUE )
    lcd.print( "PicoGo", c=LCD.WHITE ) 
    
    lcd.print( "Hello...." )
    lcd.print( "Raspberry Pi Pico", c=LCD.BLUE )
    lcd.print( "PicoGo", c=LCD.WHITE )
    lcd.print( "Waveshare.com", c=LCD.RED ) 
    
    lcd.show()
pass