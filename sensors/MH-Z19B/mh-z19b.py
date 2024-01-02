import utime as time
from machine import Pin, I2C

# Initialize UART communication on the Raspberry Pi Pico
uart = machine.UART(1, baudrate=9600, tx=machine.Pin(4), rx=machine.Pin(5))

def read_mhz19b():
    # Command to request CO2 data from MH-Z19B
    command = bytearray(b'\xff\x01\x86\x00\x00\x00\x00\x00\x79')
    uart.write(command)
    
    # Wait for the sensor to respond
    time.sleep_ms(100)
    
    # Read the response
    result = uart.read(9)
    
    if result is None or len(result) != 9:
        return None
    
    high, low = result[2], result[3]
    co2 = (high << 8) | low
    
    return co2

while True:
    co2_value = read_mhz19b()
    if co2_value:
        print("CO2:", co2_value, "ppm")
    else:
        print("Failed to read CO2 value")
    
    time.sleep(10)

