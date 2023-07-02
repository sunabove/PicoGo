from time import sleep

from picogo.Motor import Motor
from picogo.LCD import LCD
from picogo.IRSensor import IRSensor

if __name__ == '__main__' :
    
    motor = Motor()
    lcd = LCD()
    irSensor = IRSensor()
    
    lcd.disp_init()

    speed = 20
    duration = 0.02
    
    idx = 0 
    while True:
        idx += 1
        blocks = [ left_block, right_block ] = irSensor.read_blocks()
        
        lcd.disp_ir_sensor( blocks )
        lcd.show() 
        
        print( f"[{idx:4d}] InfraRed left: {left_block}, right: {right_block}" )

        if  left_block and right_block : # 양쪽에 장애물이 있을 때, 좌회전
            motor.left( speed )
            sleep( 5*duration )
        elif left_block : # 좌측 장애물시, 우회전
            motor.right( speed )
            sleep( 5*duration )
        elif right_block :  # 우측 장애물시, 좌회전
            motor.left( speed )
            sleep( 5*duration )
        else :  # 장매물이 없으면, 전진
            motor.forward( speed )
            sleep( duration )
        pass            
        
    pass

pass