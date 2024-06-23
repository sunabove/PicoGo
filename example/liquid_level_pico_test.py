# liquid_level_pico_test.py

from machine import Pin,ADC
import utime

adc = machine.ADC(0) # ADC input 0 (GPIO26)
conv_factor = 3.3/65535 # conversion factor

count = 0 
while 1 :
    dvalue = adc.read_u16() * conv_factor

    if dvalue >= 1.0 :
        print( f"[{count:3d}] Water detected, {dvalue:.4f}" )
    else :
        print( f"[{count:3d}] No water detected, {dvalue:.4f}" )
    pass 

    utime.sleep( 1 )
    
    count += 1
pass