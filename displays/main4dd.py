from fourDigitDisplay import *
import time

dd4Port = 8

print("running")
print("Initialising 4 digit display...")
my4DD = fourDigitDisplay(dd4Port)

print("sleeping 2...")
time.sleep(2)

for i in range(0,8):
  my4DD.setBrightness(i)
  my4DD.setValue(i*93, 1)
  time.sleep(1)

for i in range(0,127):
  my4DD.setSegment(1, i)
  time.sleep(0.05)

my4DD.setSegment(1, 0)

for i in range(0,7):
  value = 2 ** i
  print("i = ", i, " value = ", value)
  my4DD.setSegment(1, value)
  time.sleep(4)

my4DD.setSegment(0, 55)
my4DD.setSegment(1, 121)
my4DD.setSegment(2, 48)
my4DD.setSegment(3, 56)
time.sleep(10)

my4DD.setScore(4, 69)
time.sleep(4)

my4DD.setDigit(0, 2)
my4DD.setDigit(1, 8)
my4DD.setDigit(2, 1)
my4DD.setDigit(3, 2)
time.sleep(5)

#my4DD.monitorAnalogue(1, 10);

time.sleep(5)


