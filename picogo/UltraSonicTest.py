from time import sleep 

from .UltraSonic import UltraSonic

if __name__=='__main__':
    ultraSonic = UltraSonic()
    
    while True:
        dist = ultraSonic.obstacle_distance()
        print( f"Distance = {dist:6.2f} cm" )
        sleep( 0.1)
    pass
pass
