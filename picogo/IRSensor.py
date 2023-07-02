from machine import Pin

class IRSensor :
    
    def __init__( self ) :
        self.ds_right = Pin(2, Pin.IN)
        self.ds_left  = Pin(3, Pin.IN)
    pass

    def read_blocks( self ) :
        return [ self.ds_left.value() == 0, self.ds_right.value() == 0 ]   # left_block, right_block
    pass

pass