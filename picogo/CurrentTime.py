import time
    
def current_time_mili():
    return round(time.time() * 1000)
pass

def curr_time_mili():
    return current_time_mili()
pass

if __name__== '__main__' :
    print( 'Hello World!' )

    print( f"curr time = {current_time_mili()}" )
    
    time.sleep( 1 )
    
    print( f"curr time = {curr_time_mili()}" )
    
pass