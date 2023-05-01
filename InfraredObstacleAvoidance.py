from Motor import PicoGo
from InfraredSensor import InfraredSensor
from time import sleep

if __name__ == '__main__' :
    
    robot = PicoGo()
    
    infraredSensor = InfraredSensor()

    speed = 20
    duration = 0.02
    
    idx = 0 
    while True:
        idx += 1
        left_block, right_block = infraredSensor.read_blocks()
        
        print( f"[{idx:4d}] InfraRed left: {left_block}, right: {right_block}" )

        if  left_block and right_block : # 양쪽에 장애물이 있을 때, 좌회전
            robot.left( speed )
            sleep( 5*duration )
        elif left_block : # 좌측 장애물시, 우회전
            robot.right( speed )
            sleep( 5*duration )
        elif right_block :  # 우측 장애물시, 좌회전
            robot.left( speed )
            sleep( 5*duration )
        else :  # 장매물이 없으면, 전진
            robot.forward( speed )
            sleep( duration )
        pass            
        
    pass

pass