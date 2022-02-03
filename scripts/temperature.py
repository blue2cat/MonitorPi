# packages needed
import os
import glob
import time
import json
import re

# import python modules
from MonitorPi import (
    read_config,
    read_temperature,
    read_temperature_raw,
    get_temperature_data_json,
)

# start GPIO pins
os.system("modprobe w1-gpio")
os.system("modprobe w1-therm")

# full path to config.txt
configPath = "/home/pi/config.txt"


# directory to look for sensors in
base_dir = "/sys/bus/w1/devices/"

# output results as JSON
print(get_temperature_data_json(configPath, base_dir))
