# Author: Andrei Pârv
# Source: https://github.com/andreip024/raspbery-pi-pico-micropython

from machine import Pin, I2C
import utime as time
import bme280


# Convert a pressure from hectoPascals to millimeters of mercury
def hpa_to_mmhg(pressure_hpa):
    return pressure_hpa * 0.750062

# Convert a temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Setup wiring pins
sda_pin = 0
scl_pin = 1

# Setup I2C
i2c=I2C(0,sda=Pin(sda_pin), scl=Pin(scl_pin), freq=400000)

# Initialize SHT21 sensor
sensor_bme280 = bme280.BME280(i2c=i2c)

while True:
    temperature_celsius_value = sensor_bme280.values[0][:-1]
    temperature_fahrenheit_value = celsius_to_fahrenheit(float(temperature_celsius_value))
    humidity_value = sensor_bme280.values[2][:-1]
    pressure_hPa_value = sensor_bme280.values[1][:-3]
    pressure_mmHg_value  = hpa_to_mmhg(float(pressure_hPa_value))

    print("Temperature =", temperature_celsius_value, "°C")
    print("Temperature =", temperature_fahrenheit_value, "°F")
    print("Humidity =", humidity_value, "%")
    print("Pressure =", pressure_hPa_value, "hPA")
    print("Pressure = ", pressure_mmHg_value, "mmHg")

    time.sleep(3)
