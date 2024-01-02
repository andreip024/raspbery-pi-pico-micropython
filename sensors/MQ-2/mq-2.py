
import utime as time
from basemq import MQ2

sensor = MQ2(pinData = 26, baseVoltage = 3.3)

print("Calibrating")
sensor.calibrate()
print("Calibration completed")
print("Base resistance: {0}".format(sensor._ro))

while True:
	print("Smoke: {:.1f}".format(sensor.readSmoke())+" ppm")
	print("LPG: {:.1f}".format(sensor.readLPG())+" ppm")
	print("Methane: {:.1f}".format(sensor.readMethane())+" ppm")
	print("Hydrogen: {:.1f}".format(sensor.readHydrogen())+" ppm")
	
	time.sleep(10)
