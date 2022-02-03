# imports
import RPi.GPIO as GPIO
import time, sys, signal, json, os, re

# checks the sensor data to see if the door is open or closed
def check_door_status(DOOR_SENSOR_PIN_START, DOOR_SENSOR_PIN_RANGE):

    PRINT_STATUS = []

    # iterate through sensors
    for x in range(DOOR_SENSOR_PIN_RANGE):

        # Initially we don't know if the door sensor is open or closed...
        IS_OPEN = None
        OLD_IS_OPEN = None

        # calculate what pin we are working with
        CURRENT_PIN = DOOR_SENSOR_PIN_START + x

        # Set up the door sensor pin.
        GPIO.setup(CURRENT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # query the pin for its status
        IS_OPEN = GPIO.input(CURRENT_PIN)

        # is the pin open or closed?
        if IS_OPEN and (IS_OPEN != OLD_IS_OPEN):
            PRINT_STATUS.append("sensor{}:closed".format(x))
        elif IS_OPEN != OLD_IS_OPEN:
            PRINT_STATUS.append("sensor{}:open".format(x))

    # return JSON data
    return json.dumps(PRINT_STATUS)


# read the raw data back from sensor
def read_raw_temperature_data(SENSOR_ID, BASE_DIR):

    # folder containing sensor data
    DEVICE_FOLDER = BASE_DIR + SENSOR_ID

    # file for data
    DEVICE_FILE = DEVICE_FOLDER + "/w1_slave"
    f = open(DEVICE_FILE, "r")
    lines = f.readlines()
    f.close()
    return lines


# return pretty data from raw data function
def read_temperature(SENSOR_ID, BASE_DIR):

    # read the output from the sensor
    lines = read_raw_temperature_data(SENSOR_ID, BASE_DIR)

    # sort through data to find raw temp
    while lines[0].strip()[-3:] != "YES":
        time.sleep(0.2)
        lines = read_raw_temperature_data(SENSOR_ID, BASE_DIR)
    EQUALS_POS = lines[1].find("t=")

    # if there is a temp, return it
    if EQUALS_POS != -1:
        temp_string = lines[1][EQUALS_POS + 2 :]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        final = str(temp_f)
        return final


# read in the temperature config file
def read_config(CONFIG_FILE_NAME):

    # open config file
    CONFIG_FILE = open(CONFIG_FILE_NAME, "r")

    # read lines
    lines = CONFIG_FILE.readlines()

    # clean up file and close
    CONFIG_FILE.close()

    # define MAC REGEX matching
    REGEX = re.compile("28*")

    # sensor list
    SENSORS = []

    # loop through lines
    COUNT = 0

    # loop through lines
    for line in lines:
        COUNT += 1
        IS_MATCH = REGEX.match(line)

        # if REGEX matches
        if IS_MATCH:
            SENSORS.append(line[:15])

    # return list of SENSORS
    return SENSORS


def get_temperature_data_json(CONFIG_FILE_NAME, BASE_DIR):

    SENSOR_DATA = []

    # read in the config file
    SENSORS = read_config(CONFIG_FILE_NAME)

    # loop through sensors
    for SENSOR_ID in SENSORS:

        # get raw data
        raw_data = read_raw_temperature_data(SENSOR_ID, BASE_DIR)

        # get temperature
        SENSOR_DATA.append(read_temperature(SENSOR_ID, BASE_DIR))

    # return JSON data
    return json.dumps(SENSOR_DATA)
