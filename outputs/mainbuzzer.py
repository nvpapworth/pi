from buzzer import *
import time

buzzerPort = 4

print("running")
print("Initialising buzzer port...")
myBuzzer = buzzer(buzzerPort)

myBuzzer.turnOn(0.5)

myBuzzer.turnOff()
time.sleep(0.5)


