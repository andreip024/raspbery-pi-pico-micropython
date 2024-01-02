import utime as time
from machine import Pin, I2C
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

pms5003 = PMS5003(
    # Initialize UART communication on the Raspberry Pi Pico
    uart=machine.UART(1, baudrate=9600, tx=machine.Pin(8), rx=machine.Pin(9)),

    # Set enable pin
    pin_enable=machine.Pin(3),

    # Set reset pin
    pin_reset=machine.Pin(2),
    mode="active"
)

while True:

    data = pms5003.read()
    link = str(data)
    lines = split_string(link, "\n")
    values = []
    lines.pop(0)
    lines.pop(-1)

    for i in lines:
        x = split_string(i, ":")
        values.append(x)

    print("PM1_0 standard: " + str(int(values[0][1])))
    print("PM2_5 standard:" + str(int(values[1][1])))
    print("PM10_standard:" + str(int(values[2][1])))
    print("PM1_0_atmospheric:" + str(int(values[3][1])))
    print("PM2_5_atmospheric:" + str(int(values[4][1])))
    print("PM10_atmospheric:" + str(int(values[5][1])))
    print("UM_0_3:" + str(int(values[6][1])))
    print("UM_0_5:" + str(int(values[7][1])))
    print("UM_1_0:" + str(int(values[8][1])))
    print("UM_2_5:" + str(int(values[9][1])))
    print("UM_5_0:" + str(int(values[10][1])))
    print("UM_10:" + str(int(values[11][1])))

    time.sleep(10)