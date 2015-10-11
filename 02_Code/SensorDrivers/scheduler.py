#!/usr/bin/python

##==============================================================================##
## FULL STACK EMBEDDED 2016                                                     ##
##==============================================================================##
## File  :       run_sht21.py                                                   ##
## Author:       FA                                                             ##
## Board :       Raspberry Pi                                                   ##
## Brief :       Scheduler                                                      ##
## Note  :                                                                      ##
##==============================================================================##

from sht21_class import TemperatureSensor, HumiditySensor
from mpl3115a2_class import AirPressureSensor
import time

count = 0
if __name__ == "__main__":
    """
    Prototype sensor polling scheduler.

    To be implemented:
    1. The value read from the sensor ``val`` needs to be saved
    in a file. Also, the file per sensor needs to be determined.

    2. Logic for failed sensor readings
    """
    start = time.time()
    sensor_list = [(TemperatureSensor(), 1, "/dev/temperature-sensor"),
                   (HumiditySensor()   , 1, "/dev/humidity-sensor"),
                   (AirPressureSensor(), 1, "/dev/Pressure-sensor")]
    while True:
        runtime = int(time.time() - start)
        for sensor, interval, logfile in sensor_list:
            if not runtime % interval:
                val = sensor.get_value()
                if not count % 3:
                    print('------------------------------------------------')
                count = count+1
        time.sleep(0.8)