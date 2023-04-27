from LCD import LCD 
        
if __name__=='__main__':
    lcd = LCD()
    
    lcd.print( "Hello...." )
    lcd.print( "Raspberry Pi Pico", c=LCD.BLUE )
    lcd.print( "PicoGo", c=LCD.WHITE )
    lcd.print( "Waveshare.com", c=0x07E0 )
    
    lcd.print( "Goood bye!" ) 
pass