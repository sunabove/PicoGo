from LCD import LCD
from Battery import Battery
from time import sleep
from random import randint
        
if __name__=='__main__': 
    
    lcd = LCD()
    
    from Battery import Battery
    
    battery = Battery()
    
    while True :
        
        lcd.disp_battery( battery )
        lcd.show()
        
        sleep( 1 )
    pass 
pass