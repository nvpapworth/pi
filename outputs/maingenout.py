from genericDigitalOnOff import *
import time

buzzerPort = 4

print("running")
print("Initialising buzzer port...")
myBuzzer = genericDigitalOnOff("buzzer", buzzerPort)

myBuzzer.turnOnWait(0.5)

myBuzzer.turnOff()
time.sleep(0.5)


