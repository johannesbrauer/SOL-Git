from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms

led = Pin(13, Pin.OUT)
led.value(1)

pixels_count = 32
pixels = NeoPixel(Pin(15), pixels_count)
pixels_count_half = int(pixels_count/2)

def color_by_position(offset_unlimited):
    ## This function accepts any values as offset.
    ## For the following calculation we limit offset to be a value between 0 and pixels_count
    offset = offset_unlimited % pixels_count

    ## brightness should be a value between 0 and 1
    ## in this example we use a linear interpolation from 0 via 1 to 0
    brightness = abs(offset-pixels_count_half) / pixels_count_half

    ## The result is a 8bit integer and can be used as rgb-color-component
    return int(255*brightness)

t = 0
while True:
    t += 1

    ## Use the Modulo-Operator to blink a LED
    led.value(t%2)

    ## Set a color for each of the RGB-LEDs
    for i in range(pixels_count):
        r = color_by_position(i-t)
        g = color_by_position(i-t + int(pixels_count*1/3))
        b = color_by_position(i-t + int(pixels_count*2/3))
        pixels[i] = (r, g, b)

    ## Sort pixels by the red component using bubble sort
    for i in range(pixels_count):
        for j in range(0, pixels_count - i - 1):
            ## Check if the red value (index 0) of the current pixel is greater than the next
            if pixels[j][0] > pixels[j + 1][0]:
                pixels[j], pixels[j + 1] = pixels[j + 1], pixels[j]

    pixels.write()
    sleep_ms(100)