from time import sleep
from picozero import Speaker, LED

led = LED(25)
speaker = Speaker(4)

BEAT = 0.4

notes_map = { "do": "c3", "re" : "d3", "mi" : "e3", "fa" : "f3", "so": "g3", "sol": "g3", "la" : "a4", "si" : "b4",
              "do+": "c4", "re+" : "d4", "mi+": "e4" }

song_0 = """do, do, sol, sol, la, la, sol2, fa, fa, mi, mi, re, re, do2,
sol, sol, fa, fa, mi, mi, re2, sol, sol, fa, fa, mi, mi, re2,
do, do, sol, sol, la, la, sol2, fa, fa, mi, mi, re, re, do2,
"""

song_1 = "sol sol la la sol sol mi2 sol sol mi mi re2 sol sol la la sol sol mi2 sol mi re mi do2"

song_2 = """sol2, la, sol2, la, sol, mi, re, do2, do+2, la, sol2, mi, sol2,
la, la, sol, la, sol, mi, re, do2, re, mi, re, mi, do2,
re, re, do, re, mi, mi, do2, la, sol, la, si, do+, sol2,
do+, ra, sol, mi, re, mi, sol, la2, sol2, re, fa, mi, re, do2
"""

songs = [ song_0, song_1, song_2 ]

def to_melody( song ) :
    notes = []
    song = song.replace( ",", " " )
    song = song.split( " " )
    
    for s in song :
        beat_ratio = 1
        
        s = s.strip()
        
        if len( s ) < 1 :
            continue
        
        if s[-1].isdigit():
            beat_ratio = 2
            s = s[0:-1]
        pass
    
        if s in notes_map :
            note = notes_map[ s ]
            notes.append( [ note, BEAT*beat_ratio ] )
        else :
            print( f"invalid note = {s}" )
    pass

    return notes
pass

sleep( 1 )

try :
    print( "hello" )
    for song in songs : 
        led.toggle()
        speaker.play( to_melody( song ) )
        sleep( 3 )
    pass
except :
    pass
finally:
    led.off()
pass
