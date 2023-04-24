from machine import Pin
from LCD import LCD
from time import sleep

if __name__ == '__main__' : 
    bat = machine.ADC(Pin(26))
    temp = machine.ADC(4)

    lcd = LCD()
    lcd.fill(0xF232)
    lcd.line(2,2,70,2,0xBB56)
    lcd.line(70,2,85,17,0xBB56)
    lcd.line(85,17,222,17,0xBB56)
    lcd.line(222,17,237,32,0xBB56)
    lcd.line(2,2,2,118,0xBB56)
    lcd.line(2,118,17,132,0xBB56)
    lcd.line(17,132,237,132,0xBB56)
    lcd.line(237,32,237,132,0xBB56)

    lcd.text("Raspberry Pi Pico",90,7,0xFF00)
    lcd.text("PicoGo",10,7,0x001F)
    lcd.text("Waveshare.com",70,120,0x07E0)
    lcd.show()

    count = 1
    while True :
        reading = temp.read_u16() * 3.3 / (65535)
        temperature = 27 - (reading - 0.706)/0.001721
        v = bat.read_u16()*3.3/65535 * 2
        p = (v - 3) * 100 / 1.2
        
        if(p < 0): p=0
        if(p > 100): p=100

        y = 35
        lcd.fill_rect(30, y, 120, 40,0xF232)
        lcd.text( f"count : {count}", 30, y, 0xFFFF ); y += 15
        lcd.text( f"temperature : {temperature:5.2f} C", 30, y, 0xFFFF ); y += 15
        lcd.text( f"Voltage     : {v:5.2f} V", 30, y, 0xFFFF ); y += 15
        lcd.text( f"percent     : {p:3.1f} %", 30, y, 0xFFFF ); y += 15

        lcd.show()
        sleep( 1 )
        count += 1
    pass

pass