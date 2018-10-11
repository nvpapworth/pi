import sys
import time
from threading import Timer
import math
import grovepi

class buzzer:

   def __init__(self, port):
      print("Initialising buzzer digital port", port)
      self.buzzerGrovePort = port
      self.buzzer_state = 0
      grovepi.pinMode(self.buzzerGrovePort, "OUTPUT")

   def __del__(self):
      print("destructor for buzzer port", self.buzzerGrovePort)
      grovepi.pinMode(self.buzzerGrovePort, "INPUT")

   def turnOn(self, seconds):
      print("buzzer on...")
      self.buzzer_state = 1
      grovepi.digitalWrite(self.buzzerGrovePort, 1)
      time.sleep(seconds)
      print("buzzer off...")
      grovepi.digitalWrite(self.buzzerGrovePort, 0)
      self.buzzer_state = 0
      return;

   def turnOffAsync(self):
      print("buzzer off for async call...")
      grovepi.digitalWrite(self.buzzerGrovePort, 0)
      self.buzzer_state = 0
      return;

   def turnOnAsync(self, seconds):
      print("buzzer on async for", seconds, "seconds")
      self.buzzer_state = 1
      grovepi.digitalWrite(self.buzzerGrovePort, 1)
      Timer(seconds, self.turnOffAsync, ()).start()
      return;

   def turnOff(self):
      print("buzzer off...")
      grovepi.digitalWrite(self.buzzerGrovePort, 0)
      self.buzzer_state = 0
      return;

   def getState(self):
      print 'buzzer state =', self.buzzer_state
      return self.buzzer_state;



