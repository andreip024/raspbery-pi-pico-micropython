# Author: Andrei Pârv
# Source: https://github.com/andreip024/raspbery-pi-pico-micropython

import utime as time
from mhz19 import MHZ19


# Setup wiring pins
tx_pin = 4 #GP4
rx_pin = 5 #GP5

# Initialize UART communication on the Raspberry Pi Pico
mhz19 = MHZ19(
        uart = machine.UART(1, baudrate=9600, tx=machine.Pin(tx_pin), rx=machine.Pin(rx_pin))
)

# Calibrate the sensor
# mhz19.calibrate()

while True:
    co2_value = mhz19.read_mhz19()

    print("CO2:", co2_value, "ppm")

    time.sleep(3)
