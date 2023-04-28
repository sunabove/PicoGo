from LCD import LCD
from Battery import Battery
from time import sleep
from random import randint
        
if __name__=='__main__': 
    
    lcd = LCD()
    
    lcd.fill( lcd.BLACK )
    lcd.show()
    
    from Battery import Battery
    
    battery = Battery()
    
    idx = 0
    while True :
        idx += 1
        
        values = [ temp, voltage, percent ] = battery.read()
        
        #values = [ temp,  voltage, randint( 0, 100 ) ] 
        
        lcd.disp_battery( values )
        lcd.show()
        
        sleep( 1 )
    pass 
pass