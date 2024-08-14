# picozero 라이브러리에서 DistanceSensor 클래스 사용
from picozero import DistanceSensor
# 시간 지연을 위해 time 모듈에서 sleep 함수를 사용
from time import sleep

# 초음파 거리 센서 초기화
distanceSensor = DistanceSensor(trigger=20, echo=12)

# 무한 루프를 실행합니다. 
# 사용자가 강제로 중지하기 전까지 계속 반복됩니다.
while 1 :
    # 현재 측정된 거리를 센티미터(cm) 단위로 출력합니다.
    # 측정된 거리는 소수점 세 자리까지 표시됩니다.
    print( f"{distanceSensor.distance * 100:6.3f} cm" )
    
    sleep(0.1)  # 0.1초 동안 대기합니다. 초당 약 10번 측정합니다.
pass
