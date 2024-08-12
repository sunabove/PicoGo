# picozero 패키지의 LED와 Button 임포트
from picozero import LED, Button

led = LED(17)  # GPIO 17번 핀에 연결된 LED 생성
button = Button(2)  # GPIO 2번 핀에 연결된 버튼 생성

# 버튼이 눌렸을 때, LED를 켜는 함수를 실행
button.when_pressed = led.on
# 버튼이 떼어졌을 때, LED를 꺼는 함수를 실행
button.when_released = led.off

# 사용자가 Enter 키를 입력 시까지 대기
input( "Enter to quit!" )