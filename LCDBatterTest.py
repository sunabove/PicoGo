from LCD import LCD
from Battery import Battery
from time import sleep
        
if __name__=='__main__': 
    
    lcd = LCD()
    
    lcd.fill( lcd.BLACK )
    lcd.show()
    
    battery = Battery()
    
    idx = 0
    while True :
        idx += 1
        
        values = temperature, voltage, percent = battery.read()
        
        lcd.disp_battery( values )
        lcd.show()
        
        sleep( 0.1 )
    pass 
pass