print( "\nHello ...\n" )

import os, wave as wave_reader
from picozero import Speaker, LED
from time import sleep
import struct

led = LED(25)
speaker = Speaker(4)

led.on()

folder = "/sounds"

for file_name in sorted( os.listdir( folder ) ) :
    path = f"{folder}/{file_name}"
    wav = f = wave_reader.open( path, "rb" )
    print( f"{file_name:<40} framerate: {f.getframerate():>5,}, sampwidth: {f.getsampwidth():>5,} channels: {f.getnchannels():>6}, frames: {f.getnframes():>6,}" )
    channels = f.getnchannels()
    if channels == 1 :
        framerate = f.getframerate()
        frameCount = f.getnframes()
        beat = 1/framerate
        
        print( f"beat = {beat}" )
        
        frames = f.readframes(-1)
        for idx in range( frameCount ) :
            freq = frames[2*idx + 1]*255 + frames[2*idx]
            #print( f"freq = {freq}" )
            speaker.play( freq, beat )
        pass
    else :
        print( f"Invalid channel = {channels}" )
    pass

    f.close()
    
    break
pass

led.off()

print( "\nGood bye!\n" )