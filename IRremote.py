from machine import Pin
from Motor import PicoGo
from time import sleep_us

def getkey():
    IR = Pin(5, Pin.IN)
    
    if (IR.value() == 0):
        count = 0
        while ((IR.value() == 0) and (count < 100)): #9ms
            count += 1
            sleep_us(100)
        if(count < 10):
            return None
        count = 0
        while ((IR.value() == 1) and (count < 50)): #4.5ms
            count += 1
            sleep_us(100)
            
        idx = 0
        cnt = 0
        data = [0,0,0,0]
        for i in range(0,32):
            count = 0
            while ((IR.value() == 0) and (count < 10)):    #0.56ms
                count += 1
                sleep_us(100)

            count = 0
            while ((IR.value() == 1) and (count < 20)):   #0: 0.56mx
                count += 1                                #1: 1.69ms
                sleep_us(100)

            if count > 7:
                data[idx] |= 1<<cnt
            if cnt == 7:
                cnt = 0
                idx += 1
            else:
                cnt += 1

        if data[0]+data[1] == 0xFF and data[2]+data[3] == 0xFF:  #check
            return data[2]
        else:
            return("repeat")

if __name__=='__main__':
    
    M = PicoGo()
    speed = 20
    
    while True:
        key = getkey()
        if(key != None):
            if key == 0x18:
                M.forward(speed)
                print("forward")
            elif key == 0x08:
                M.left(20)
                print("left")
            elif key == 0x1c:
                M.stop()
                print("stop")
            elif key == 0x5a:
                M.right(20)
                print("right")
            elif key == 0x52:
                M.backward(speed)
                print("backward")
            elif key == 0x09:
                speed = 50
                print(speed)
            elif key == 0x15:
                if(speed + 10 < 101):
                    speed += 10
                print(speed)
            elif key == 0x07:
                if(speed - 10 > -1):
                    speed -= 10
                print(speed)
            pass
        pass
    pass
pass
