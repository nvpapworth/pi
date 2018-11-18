
from usbGps import *
import json
import time

# USB port
usbPort = "/dev/ttyUSB0"
baud = 4800
timeout = 0

print("running")
print("Initialising USB GPS...")
myGps = usbGps(usbPort, baud, timeout)

print("sleeping 1...")
time.sleep(1)

while True:
   try:

    in_data = myGps.read()
    if in_data != []:
      print (json.dumps(in_data))

      time.sleep(1)

   except IOError:
        print ("Error")

