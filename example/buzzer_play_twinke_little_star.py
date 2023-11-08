from time import sleep
from picozero import Speaker, LED

led = LED(25)
speaker = Speaker(4)

BEAT = 0.4

melodies = [
    ['c3', BEAT ], ['c3', BEAT ], ['g3', BEAT ], ['g3', BEAT ], ['a4', BEAT ], ['a4', BEAT ], ['g3', BEAT*2 ],
    ['f3', BEAT ], ['f3', BEAT ], ['e3', BEAT ], ['e3', BEAT ], ['d3', BEAT ], ['d3', BEAT ], ['c3', BEAT*2 ],
    
    ['g3', BEAT ], ['g3', BEAT ], ['f3', BEAT ], ['f3', BEAT ], ['e3', BEAT ], ['e3', BEAT ], ['d3', BEAT*2 ],
    ['g3', BEAT ], ['g3', BEAT ], ['f3', BEAT ], ['f3', BEAT ], ['e3', BEAT ], ['e3', BEAT ], ['d3', BEAT*2 ],
    
    ['c3', BEAT ], ['c3', BEAT ], ['g3', BEAT ], ['g3', BEAT ], ['a4', BEAT ], ['a4', BEAT ], ['g3', BEAT*2 ],
    ['f3', BEAT ], ['f3', BEAT ], ['e3', BEAT ], ['e3', BEAT ], ['d3', BEAT ], ['d3', BEAT ], ['c3', BEAT*2 ],
]

sleep( 1 )

try :
    for _ in range( 2 ) :
        led.toggle()
        speaker.play( melodies )
        sleep( 3 )
    pass
except :
    pass
finally:
    led.off()
pass
