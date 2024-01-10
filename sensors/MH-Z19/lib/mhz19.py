#Author: Andrei Pârv
#Source: https://github.com/andreip024/raspbery-pi-pico-micropython

from machine import Pin, I2C
import utime as time

class MHZ19:
    def __init__(self, uart):
        # Initialize UART communication on the Raspberry Pi Pico
        self.uart = uart


    def read_mhz19(self):
        # Command to request CO2 data from MH-Z19
        reading_command = bytearray(b'\xff\x01\x86\x00\x00\x00\x00\x00\x79')
        self.uart.write(reading_command)
        
        # Wait for the sensor to respond
        time.sleep_ms(100)
        
        # Read the response
        result = self.uart.read(9)
        
        if result is None or len(result) != 9:
            return None
        
        high, low = result[2], result[3]
        co2 = (high << 8) | low
        
        return co2
    
    def calibrate(self):
        print("Starting MH-Z19 sensor calibration...")
        
        calibration_command = bytearray(b'\xff\x01\x87\x00\x00\x00\x00\x00\x00\x78')
        self.uart.write(calibration_command)

        # Wait for the sensor to process the calibration command
        time.sleep_ms(100)
        
        print("Calibration completed!")



