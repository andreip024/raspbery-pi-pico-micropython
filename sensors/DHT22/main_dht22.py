# Author: Andrei Pârv
# Source: https://github.com/andreip024/raspbery-pi-pico-micropython

from machine import Pin
import utime as time
import dht


# Convert a temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Setup wiring pins
data_pin = 4

# Initialize DHT22 sensor
sensor_dht22 = dht.DHT22(machine.Pin(data_pin))

while True:
    sensor_dht22.measure()

    temperature_celsius_value = sensor_dht22.temperature()
    temperature_fahrenheit_value = celsius_to_fahrenheit(temperature_celsius_value)
    humidity_value = sensor_dht22.humidity()
    
    print("Temperature Celsius:", temperature_celsius_value, "°C")
    print("Temperature Fahrenheit:", temperature_fahrenheit_value, "°F")
    print("Humidity:", humidity_value, "%")

    time.sleep(3)
