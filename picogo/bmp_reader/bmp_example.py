from bmp_reader import BMPReader
from picogo.LCD import LCD

print( "Hello.." )

file_path = 'bmp_example.bmp'
file_path = "pico_bot_240_135.bmp"
file_path = "LogoImage_46_30.bmp"

img = BMPReader( file_path )

pixel_grid = img.get_pixels()

lcd = LCD()

def to_rgb_565( rgb ):
    red     = rgb[0]
    green   = rgb[1]
    blue    = rgb[2]
    # take in the red, green and blue values (0-255) as 8 bit values and then combine
    # and shift them to make them a 16 bit hex value in 565 format. 
    return ((int(red / 255 * 31) << 11) | (int(green / 255 * 63) << 5) | (int(blue / 255 * 31)))
pass

for row in range( img.height ):
    for col in range( img.width ):
        # The Unicorn Hat arranges its pixels starting top-right and alternates
        # back and forth with each row so we need to reverse the even rows
        if row % 2 == 0:
            col = img.width - 1 - col
        pass

        pixel = pixel_grid[row][col]
        
        c = to_rgb_565( pixel )
        
        print( f"pixel = {pixel}, c = {c}" );
        
        lcd.pixel( col, row, c )
    pass
pass

lcd.show()

print( "Good bye!" )