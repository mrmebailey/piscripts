# Imports
from machine import Pin
from neopixel import NeoPixel
import time

# LED details
GPIOnumber = 2
LEDcount = 15

# Define the strand pin number and number of LEDs from variables
strand = NeoPixel(Pin(GPIOnumber), LEDcount)

# LED index list
ledindex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# Start the strand red at low intensity
strand.fill((10,0,0))
strand.write()
time.sleep(1)

while True:
    
    # Iterate over each LED
    for led in ledindex:
        
        # Fade in/out each iterated LED
        for i in range(255,10,-1):
            
            strand[led] = (i,0,0) # Use i value for the R in RGB
            strand.write()
            time.sleep(0.001) # Fast delay
