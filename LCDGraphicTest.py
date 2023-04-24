from LCD import LCD
        
if __name__=='__main__':
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

    lcd.text("Raspberry Pi Pico", 90, 7, 0xFF00)
    lcd.text("PicoGo", 10, 7, 0x001F)
    lcd.text("Waveshare.com", 70, 120, 0x07E0)
    
    lcd.fill_rect( 30, 35, 160, 80, 0xF232 )
    lcd.rect( 30, 35, 160, 80, lcd.WHITE ) 
        
    lcd.show() 
        
pass