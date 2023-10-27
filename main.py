if __name__== '__main__' :
    
    import sys
    
    print( f'System Version = {sys.version}' )
    print( 'Hello PicoGo!' )
    print( 'Running Bluetooth program ... ' )
        
    from picogo import BlueTooth
    
    BlueTooth.main()
    
    print( "Good bye!" )
    
pass