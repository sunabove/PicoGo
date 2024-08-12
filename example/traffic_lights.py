from picozero import LED, Button
from time import sleep, time

# 버튼과 신호등 초기화
button = Button(16) # GPIO 핀 16에 연결된 버튼을 설정

# 신호등 및 관련 타이밍 설정
lights = [ LED(28), LED(27), LED(26)] # 빨강, 노랑, 초록 순서의 신호등 리스트
durations = [5, 3, 10] # 각 신호등이 켜져 있을 시간 (초)

light_no = 0   # 현재 신호등 인덱스
signal_no = 0  # 신호 변경 카운터

# 신호를 변경하는 함수
def change_signal():
    global light_no, signal_no
    signal_no += 1  # 신호 변경 카운터 증가
    light_no += 1   # 다음 신호등으로 이동
pass

# 버튼이 눌렸을 때 change_signal 함수가 실행되도록 설정
button.when_pressed = change_signal

# 무한 루프 시작
while True:
   # 모든 신호등을 꺼둠
   for light in lights:
      light.off()
   pass

   # 신호등 인덱스가 리스트 범위를 넘지 않도록 조정
   light_no = light_no % len(lights)  
   curr_signal_no = signal_no         # 현재 신호 번호 저장

   light = lights[light_no]           # 현재 켜야 할 신호등 선택
   duration = durations[light_no]     # 현재 신호등이 켜질 시간 설정
   
   start_time = time()  # 신호등 시작 시간을 기록
   elapsed = 0          # 경과 시간 초기화

   # 현재 신호가 유효하고, 경과 시간이 지정된 시간을 넘지 않을 때까지 신호등 깜빡임
   period = 0 
   while curr_signal_no == signal_no and elapsed < duration:
      if duration - elapsed <= 2 : 
         # 남은 시간이 2초 이내일 때 신호등 점멸
         period += 1
         if period%2 : light.off()
         else : light.on()
      else:
         light.on() # 신호등 켜기
      pass

      sleep(0.25)  # 짧은 지연 시간 설정
      elapsed = time() - start_time  # 경과 시간 업데이트
   pass

   # 신호 번호가 변경되지 않았으면 다음 신호등으로 이동
   if curr_signal_no == signal_no:
      light_no += 1
   pass
pass
