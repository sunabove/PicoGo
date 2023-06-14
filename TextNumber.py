numbers = [

    '''  ___  
 / _ \ 
| | | |
| | | |
| |_| |
 \___/ '''
    ,
    
    ''' __ 
/_ |
 | |
 | |
 | |
 |_|'''
    ,
    ''' ___  
|__ \ 
   ) |
  / / 
 / /_ 
|____|'''
    ,
    ''' ____  
|___ \ 
  __) |
 |__ < 
 ___) |
|____/ '''
    ,
    
    ''' _  _   
| || |  
| || |_ 
|__   _|
   | |  
   |_| '''
    ,
        
    ''' _____ 
| ____|
| |__  
|___ \ 
 ___) |
|____/ '''
    ,
        
    '''   __  
  / /  
 / /_  
| '_ \ 
| (_) |
 \___/ '''
    ,
        
    ''' ______ 
|____  |
    / / 
   / /  
  / /   
 /_/    '''
    ,
        
    '''  ___  
 / _ \ 
| (_) |
 > _ < 
| (_) |
 \___/ '''
    ,
        
    '''  ___  
 / _ \ 
| (_) |
 \__, |
   / / 
  /_/  '''
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