from LCD import LCD
        
if __name__=='__main__':
    lcd = LCD()
    
    width = lcd.width
    height = lcd.height
    
    lcd.fill( lcd.WHITE )
    
    x = 10; y = 10;  w = width
    
    # 선 그리기 
    lcd.line( x, y, x + w - 2*x - 1 , y, lcd.BLUE )
    
    # 사각형 채우기    
    y = 20 ; h = 20
    lcd.rect( x, y, w - 2*x - 1 , h, lcd.YELLOW, True )
    
    # 사각형 외곽선 그리기 
    y += h + 10 ; h = 20
    lcd.rect( x, y, w - 2*x - 1 , h, lcd.RED, False ) 
        
    lcd.show() 
        
pass