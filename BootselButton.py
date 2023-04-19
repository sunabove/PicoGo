from time import sleep
from machine import Pin
from rp2 import bootsel_button

print( "Hello ...." )

led = Pin( 25, Pin.OUT)

while not bootsel_button() :
  led.toggle()
  sleep( 0.1 )
pass

print( "Bootsel pressed!" )
print( "Good bye!" )