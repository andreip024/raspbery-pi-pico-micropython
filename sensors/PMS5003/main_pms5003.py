# Author: Andrei Pârv
# Source: https://github.com/andreip024/raspbery-pi-pico-micropython

from machine import Pin, I2C
import utime as time
from pms5003 import PMS5003


# Defines a spliter of strings to return each value independently
def split_string(string, delimiter):
    parts = []
    current_part = ""
    for char in string:
        if char == delimiter:
            parts.append(current_part)
            current_part = ""
        else:
            current_part += char
    parts.append(current_part)
    return parts

# Setup wiring pins
tx_pin = 8 #GP8
rx_pin = 9 #GP9
enable_pin = 3 #GP3
reset_pin = 2 #GP2

# Set operational mode "active" or "passive"
mode="active"

# Initialize UART communication on the Raspberry Pi Pico
pms5003 = PMS5003(
    uart=machine.UART(1, baudrate=9600, tx=machine.Pin(tx_pin), rx=machine.Pin(rx_pin)),
    pin_enable=machine.Pin(enable_pin),
    pin_reset=machine.Pin(reset_pin),
    mode=mode
)

while True:
    sensor_pms5003 = pms5003.read()

    link = str(sensor_pms5003)
    lines = split_string(link, "\n")
    values = []
    lines.pop(0)
    lines.pop(-1)

    for i in lines:
        x = split_string(i, ":")
        values.append(x)

    pm1_standard_value = str(int(values[0][1]))
    pm2_5_standart_value = str(int(values[1][1]))
    pm10_standard_value = str(int(values[2][1]))
    pm1_atmos_env_value = str(int(values[3][1]))
    pm2_5_atmos_env_value = str(int(values[4][1]))
    pm10_atmos_env_value = str(int(values[5][1]))
    particle_03um_value = str(int(values[6][1]))
    particle_05um_value = str(int(values[7][1]))
    particle_1um_value = str(int(values[8][1]))
    particle_25um_value = str(int(values[9][1]))
    particle_5um_value = str(int(values[10][1]))
    particle_10um_value = str(int(values[11][1]))

    print("PM1_0 standard:", pm1_standard_value, "μg/m3")
    print("PM2_5 standard:", pm2_5_standart_value, "μg/m3" )
    print("PM10_standard:", pm10_standard_value, "μg/m3")
    print("PM1_0_atmospheric:" , pm1_atmos_env_value, "μg/m3")
    print("PM2_5_atmospheric:", pm2_5_atmos_env_value, "μg/m3")
    print("PM10_atmospheric:", pm10_atmos_env_value, "μg/m3")
    print("UM_0_3:", particle_03um_value, "um/0.1l")
    print("UM_0_5:", particle_05um_value, "um/0.1l")
    print("UM_1_0:", particle_1um_value, "um/0.1l")
    print("UM_2_5:", particle_25um_value, "um/0.1l")
    print("UM_5_0:", particle_5um_value, "um/0.1l")
    print("UM_10:", particle_10um_value, "um/0.1l")

    time.sleep(3)