import builtins

def print(*args, **kwargs): 
    builtins.print( "Hello...." )
    builtins.print( *args, **kwargs )

print('the answer is', 1 + 2)