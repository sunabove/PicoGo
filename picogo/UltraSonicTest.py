from time import sleep 

from picogo.UltraSonic import UltraSonic

if __name__ is '__main__':
    ultraSonic = UltraSonic()
    
    while True:
        dist = ultraSonic.distance()
        print( f"Distance = {dist:6.2f} cm" )
        sleep( 0.1)
    pass
pass
