numbers = [

    '''
  ___  
 / _ \ 
| | | |
| | | |
| |_| |
 \___/ '''[ 1 : ]
    ,
    
    '''
 __ 
/_ |
 | |
 | |
 | |
 |_|'''[ 1 : ]
    ,
    '''
 ___  
|__ \ 
   ) |
  / / 
 / /_ 
|____|'''[ 1 : ]
    ,
    '''
 ____  
|___ \ 
  __) |
 |__ < 
 ___) |
|____/ '''[ 1 : ]
    ,
    
    '''
 _  _   
| || |  
| || |_ 
|__   _|
   | |  
   |_| '''[ 1 : ]
    ,
        
    '''
 _____ 
| ____|
| |__  
|___ \ 
 ___) |
|____/ '''[ 1 : ]
    ,
        
    '''
   __  
  / /  
 / /_  
| '_ \ 
| (_) |
 \___/ '''[ 1 : ]
    ,
        
    '''
 ______ 
|____  |
    / / 
   / /  
  / /   
 /_/    '''[ 1 : ]
    ,
        
    '''
  ___  
 / _ \ 
| (_) |
 > _ < 
| (_) |
 \___/ '''[ 1 : ]
    ,
        
    '''
   ___  
 / _ \ 
| (_) |
 \__, |
   / / 
  /_/  '''[ 1 : ]
    ,
    ]


if __name__ == '__main__' :
    print( "Hello NumberText test" )
    
    from LCD import LCD
    from time import sleep
    
    lcd = LCD()
    
    for number in numbers : 
        lcd.disp_full_text( number, flush=True )
        sleep( 2 )
    pass
    
pass