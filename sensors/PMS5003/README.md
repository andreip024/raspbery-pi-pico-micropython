# PMS5003 Micropython and pinout for Raspberry Pi Pico W

## Particulate Matter Sensor

### Outputs

- PM 1.0 μg/m3 (ultrafine particles)
- PM 2.5 μg/m3 (combustion particles, organic compounds, metals)
- PM 10 μg/m3  (dust, pollen, mould spores)
- PM 1.0 μg/m3 (atmos env)
- PM 2.5 μg/m3 (atmos env)
- PM 10 μg/m3 (atmos env)
- >0.3 um in 0.1L air
- >0.5 um in 0.1L air
- >1.0 um in 0.1L air
- >2.5 um in 0.1L air
- >5.0 um in 0.1L air
- >10 um in 0.1L air

### Install prerequisites

- Micropython (tested with v1.20.0)
- pms5003-micropython (tested with v0.0.7) 

### Parts needed

- Raspbare Pi Pico (W)
- PMS5003 sensor
- Wires
- Breadbord (optional)

### Instructions

- Install <b>pms5003-micropython</b> driver from Packages Manager (use Thonny)
- Copy the file <b>main_pms5003.py</b> on your Raspberry Pi Pico
- Wire the parts as show in diagram below 

### Pinout

Vin -> VBUS (red)  
GND -> GND (black)  
SET -> GP3 (brown)  
TX  -> GP9 (green)  
RX  -> GP8 (white)  
RESET -> GP4 (pink)  

### Wiring Diagram

![PMS5003 Micropython and pinout for Raspberry Pi Pico W](../../img/pms5003_Raspberry_Pi_Pico_w.jpg)


