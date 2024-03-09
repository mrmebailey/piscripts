from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from dht20 import DHT20
import time

# Define LCD/sensor I2C pins/BUS/address
SDA = 14
SCL = 15
I2C_BUS = 1
LCD_ADDR = 0x27
TEMP_ADDR = 0x38

# Define LCD rows/columns
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16

# Set up LCD I2C
lcdi2c = I2C(I2C_BUS, sda=machine.Pin(SDA), scl=machine.Pin(SCL), freq=400000)
lcd = I2cLcd(lcdi2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

# Set up temperature sensor I2C
tempi2c = I2C(I2C_BUS, sda=SDA, scl=SCL)
dht20 = DHT20(TEMP_ADDR, tempi2c)

# Write static text
lcd.putstr("Temp:")

lcd.move_to(0, 1) # Move to second row
lcd.putstr("Humidity:")
    
while True:
    
    # Grab data from the sensor dictionary
    measurements = dht20.measurements
    
    # Show temp data on the first row
    lcd.move_to(12, 0) # 12th column, 1st row
    lcd.putstr(str(round(measurements['t'],1)))
    
    # Show humidity data on the second row
    lcd.move_to(12, 1) # 12th column, 2nd row
    lcd.putstr(str(round(measurements['rh'],1)))
    
    time.sleep(5)
