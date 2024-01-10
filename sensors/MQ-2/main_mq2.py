# Author: Andrei Pârv
# Source: https://github.com/andreip024/raspbery-pi-pico-micropython

import utime as time
from basemq import MQ2


# Setup wiring pins
a0_pin = 26 #GP26

# Initialize MQ2 sensor
sensor_mq2 = MQ2(pinData = a0_pin, baseVoltage = 3.3)

# Calibrate the sensor
sensor_mq2.calibrate()

while True:
	smoke_value = sensor_mq2.readSmoke()
	lpg_value = sensor_mq2.readLPG()
	methane_value = sensor_mq2.readMethane()
	hydrogen_value = sensor_mq2.readHydrogen()

	print("Smoke:", smoke_value, "ppm")
	print("LPG:", lpg_value, "ppm")
	print("Methane:", methane_value, "ppm")
	print("Hydrogen:", hydrogen_value, "ppm")
	
	time.sleep(3)
