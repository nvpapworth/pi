from LSM6DS3 import *
from time import sleep

mySensor = LSM6DS3()

while True:
    print(mySensor.readRawAccelX(), \
        mySensor.readRawAccelY(), \
        mySensor.readRawAccelZ(), \
        mySensor.readRawGyroX(), \
        mySensor.readRawGyroY(), \
        mySensor.readRawGyroZ())
    sleep(0.08)
