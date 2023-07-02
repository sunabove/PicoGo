from time import sleep 

from picogo.LCD import LCD
from picogo.UltraSonic import UltraSonic
        
if __name__=='__main__': 
    
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
pass