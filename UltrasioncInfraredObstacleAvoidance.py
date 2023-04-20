from machine import Pin
from Motor import PicoGo
from UltrasonicRange import get_obstacle_distance
from time import sleep

if __name__ == '__main__' :

    robot = PicoGo()
    
    dsr = Pin(2, Pin.IN)
    dsl = Pin(3, Pin.IN)
    
    duration = 0.1
    speed = 30
    max_dist = 15
    
    obstacle_cnt = 0 
        
    while True:
        dist = get_obstacle_distance()
        dr_status = dsr.value()
        dl_status = dsl.value()
        
        if dist < max_dist or dl_status*dr_status == 0 :
            obstacle_cnt += 1
        pass
    
        if obstacle_cnt == 1 :
            robot.stop()
            sleep( duration)
        pass
    
        if (dl_status == 0) and (dr_status == 0) : # 양쪽에 장애물이 있을 때, 좌회전
            robot.left( speed )
        elif (dl_status == 0) and (dr_status == 1) : # 좌측 장애물시, 우회전
            robot.right( speed )
        elif (dl_status == 1) and (dr_status == 0) :  # 우측 장애물시, 좌회전
            robot.left( speed )
        elif dist < max_dist :
            robot.right( speed )    
        else :  # 장매물이 없으면, 전진
            obstacle_cnt = 0 
            robot.forward( speed )
        pass
            
        sleep( duration )
    pass

pass
