# imports
from monitorpi import check_door_status
import RPi.GPIO as GPIO
import time
import sys
import signal
import json

# set Broadcom mode so we can address GPIO pins by number.
GPIO.setmode(GPIO.BCM)

# this is the first of two gpio pins we will use.
# put the white wire of the first sensor into a ground pin, put the black
# wire into pin 17, on the second sensor, wire to a different ground and put
# the black wire into pin 18.
DOOR_SENSOR_PIN_START = 17

# this is the number of sensors you have. You need to have
# all sensors wired in consecutively higher GPIO pins from
# DOOR_SENSOR_PIN_START. For example, if you have DOOR_SENSOR_PIN_RANGE
# set to 2, you need to have the two black wires into GPIO 17 and 18.
DOOR_SENSOR_PIN_RANGE = 2

print(check_door_status(DOOR_SENSOR_PIN_START, DOOR_SENSOR_PIN_RANGE))
