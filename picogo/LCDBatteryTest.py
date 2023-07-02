from random import randint
from time import sleep

from picogo.LCD import LCD
from picogo.Battery import Battery

if __name__=='__main__': 
    
    lcd = LCD()
    battery = Battery()
    
    lcd.disp_init()
    
    while True :
        
        lcd.disp_battery( battery )
        lcd.show()
        
        sleep( 1 )
    pass 
pass