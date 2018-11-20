
import grovepi
import serial, time, sys
import re
import json
from decimal import *

en_debug = False
#en_debug = 1

def debug(in_str):
    if en_debug:
        print(in_str)

patterns_gpgga=["$GPGGA",
    "/[0-9]{6}\.[0-9]{2}/", # timestamp hhmmss.ss
    "/[0-9]{4}.[0-9]{2,/}", # latitude of position
    "/[NS]",  # North or South
    "/[0-9]{4}.[0-9]{2}", # longitude of position
    "/[EW]",  # East or West
    "/[012]", # GPS Quality Indicator
    "/[0-9]+", # Number of satellites
    "/./", # horizontal dilution of precision x.x
    "/[0-9]+\.[0-9]*/" # altitude x.x
    ]


patterns_gprmc=["$GPRMC",
    "/[0-9]{6}\.[0-9]{2}/", # timestamp hhmmss.ss
    "/[AV]",  # Status - A=data valid, V=data not valid
    "/[0-9]{4}.[0-9]{2,/}", # latitude of position
    "/[NS]",  # North or South
    "/[0-9]{4}.[0-9]{2}", # longitude of position
    "/[EW]",  # East or West
    "/[0-9]+\.[0-9]*/", # Speed Over Ground x.x
    "/[0-9]+\.[0-9]*/", # Course Over Ground x.x
    "/[0-9]{6}/", # Date ddmmyy
    ]

patterns_gpgsa=["$GPGSA",
    "/[MA]",  # Mode 1 - M=Manual, A=2D Automatic
    "/[123]" # Mode 2 - 1=Fix not available, 2=2D (less than 4 SVs used), 3=3D (more than 3 SVs used)
    ]


# GGA - GPS Fixed Data

gpsGGAFixedData = { "gpsGGA.utcTime": "000000.000",
                    "gpsGGA.latitude": "12.34",
                    "gpsGGA.NSIndicator": "X",
                    "gpsGGA.Longitude": "12.34",
                    "gpsGGA.EWIndicator": "X",
                    "gpsGGA.positionFixIndicator": 9,
                    "gpsGGA.satellitesUsed": 13,
                    "gpsGGA.HDOP": "1.1",
                    "gpsGGA.MSLAltitude.value": "12.34",
                    "gpsGGA.MSLAltitude.units": "X",
                    "gpsGGA.geoidSeparation.value": "12.34",
                    "gpsGGA.geoidSeparation.units": "X",
                    "gpsGGA.ageOfDiffCorr": "0",
                    "gpsGGA.diffRefStationId": "9999" }

gpsRMC = { "gpsRMC.utcTime": "000000.000",
           "gpsRMC.status": "X",
           "gpsRMC.latitude": "12.34",
           "gpsRMC.NSIndicator": "X",
           "gpsRMC.Longitude": "12.34",
           "gpsRMC.EWIndicator": "X",
           "gpsRMC.speedOverGround": "12.34",
           "gpsRMC.courseOverGround": "12.34",
           "gpsRMC.date": "012345",
           "gpsRMC.mode": "X" }


gpsGSA = { "gpsGSA.mode1": "X",
           "gpsGSA.mode2": "X",
           "gpsGSA.satelliteUsed01": "99",
           "gpsGSA.satelliteUsed02": "99",
           "gpsGSA.satelliteUsed03": "99",
           "gpsGSA.satelliteUsed04": "99",
           "gpsGSA.satelliteUsed05": "99",
           "gpsGSA.satelliteUsed06": "99",
           "gpsGSA.satelliteUsed07": "99",
           "gpsGSA.satelliteUsed08": "99",
           "gpsGSA.satelliteUsed09": "99",
           "gpsGSA.satelliteUsed10": "99",
           "gpsGSA.satelliteUsed11": "99",
           "gpsGSA.satelliteUsed12": "99",
           "gpsGSA.PDOP": "9.9",
           "gpsGSA.HDOP": "9.9",
           "gpsGSA.VDOP": "9.9" }


geoip = { "lat": 12.345678, 
          "lon": -123.4567890 }

geoip2 = { "lat": Decimal(12.345678), 
          "lon": Decimal(-123.4567890) }

geoip3 = { "lat": '45.5307166667', 
          "lon": '-73.507405' }

geoip4 = { "location": { "lat": 45, 
          "lon": 73 } }


class usbGps:

   def __init__(self, usbPort, baud, timeout):
      print "Initialising USB GPS device port", usbPort, "baud =",baud,"timeout =",timeout

      self.port = usbPort
      self.ser = serial.Serial(usbPort, baud, timeout=timeout)
      self.ser.flush()
      self.raw_line = ""
      self.gga = []
      self.rmc = []
      self.validation_gpgga =[] # contains compiled regex
      self.validation_gprmc =[] # contains compiled regex
      self.validation_gpgsa =[] # contains compiled regex

      # compile regex once to use later
      for i in range(len(patterns_gpgga)-1):
         self.validation_gpgga.append(re.compile(patterns_gpgga[i]))

      # compile regex once to use later
      for i in range(len(patterns_gprmc)-1):
         self.validation_gprmc.append(re.compile(patterns_gprmc[i]))

      # compile regex once to use later
      for i in range(len(patterns_gpgsa)-1):
         self.validation_gpgsa.append(re.compile(patterns_gpgsa[i]))

      self.clean_data()

      # self.get_date()  # attempt to gete date from GPS.

   def __del__(self):
      print "destructor for USB GPS device port", self.port

   def clean_data(self):

      # clean_data:
      #   ensures that all relevant GPS data is set to either empty string
      #   or -1.0, or -1, depending on appropriate type
      #   This occurs right after initialisation or
      #   after 50 attemps to reach GPS

      self.timestamp = ""
      self.lat = -1.0    # degrees minutes and decimals of minute
      self.NS = ""
      self.lon = -1.0
      self.EW = ""
      self.quality = -1
      self.satellites = -1
      self.altitude = -1.0

      self.latitude = -1.0  #degrees and decimals
      self.longitude = -1.0
      self.fancylat = ""  #

    # def get_date(self):
    #     '''
    #     attempt to get date from GPS data. So far no luck. GPS does
    #     not seem to send date sentence at all
    #     function is unfinished
    #     '''
    #     valid = False
    #     for i in range(50):
    #         time.sleep(0.5)
    #         self.raw_line = self.ser.readline().strip()
    #         if self.raw_line[:6] == "GPZDA":  # found date line!
    #             print (self.raw_line)


   def read(self):

      # Attempts 50 times at most to get valid data from GPS
      # Returns as soon as valid data is found
      # If valid data is not found, then clean up data in GPS instance

      valid = False
      for _ in range(50):
         time.sleep(0.5)
#         print "reading..."
         self.raw_line = self.ser.readline()
         try:
             self.line = self.raw_line.decode('utf-8')
             self.line = self.line.strip()
         except:
             self.line = ""
         debug(self.line)
         if self.validate(self.line):
             valid = True
             break

      if valid:
#         return self.gga
         return gpsGGAFixedData
#         return geoip4
      else:
         self.clean_data()
         return []

   def validate(self, in_line):

      # Runs regex validation on a GPGAA sentence.
      # Returns False if the sentence is mangled
      # Return True if everything is all right and sets internal
      # class members.

      if in_line == "":
         return False

      if in_line[:6] == "$GPGGA":
         gp_status = self.process_gpgga(in_line)
         return gp_status
      elif in_line[:6] == "$GPRMC":
         gp_status = self.process_gprmc(in_line)
         return gp_status
      elif in_line[:6] == "$GPGSA":
         gp_status = self.process_gpgsa(in_line)
         return gp_status
      else:
         return False


   def process_gprmc(self, in_line):
      print "$GPRMC record read ", in_line
      self.rmc = in_line.split(",")
      debug (self.rmc)

      # Sometimes multiple GPS data packets come into the stream. Take the data only after the last '$GPRMC' is seen
      try:
         ind=self.rmc.index('$GPRMC', 5, len(self.rmc))
         self.rmc=self.rmc[ind:]
      except ValueError:
         pass

      if len(self.rmc) != 13:
         debug ("Failed: wrong number of GPRMC parameters ")
         debug (self.rmc)
         return False

#      for i in range(len(self.rmc)):
#         print "rmc[", i, "] = ", self.rmc[i]

      for i in range(len(self.validation_gprmc)-1):
         if len(self.rmc[i]) == 0:
            debug ("Failed: empty string %d"%i)
            return False
         test = self.validation_gprmc[i].match(self.rmc[i])
         if test == False:
            debug ("Failed: wrong format on parameter %d"%i)
            return False
         else:
            debug("Passed %d"%i)

      try:
         self.timestamp = self.rmc[1]
         self.status = self.rmc[2]
         self.lat = float(self.rmc[3])
         self.NS = self.rmc[4]
         self.lon = float(self.rmc[5])
         self.EW = self.rmc[6]
         self.speedOverGround = float(self.rmc[7])
         self.courseOverGround = float(self.rmc[8])
         self.date = self.rmc[9]
         self.mode = self.rmc[12].split('*')[0]

         self.latitude = self.lat // 100 + self.lat % 100 / 60

         if self.NS == "S":
            self.latitude = - self.latitude

         self.longitude = self.lon // 100 + self.lon % 100 / 60

         if self.EW == "W":
            self.longitude = -self.longitude

         gpsRMC["gpsRMC.utcTime"] = self.timestamp
         gpsRMC["gpsRMC.status"] = self.status
         gpsRMC["gpsRMC.latitude"] = str(self.latitude)
         gpsRMC["gpsRMC.NSIndicator"] = self.NS
         gpsRMC["gpsRMC.Longitude"] = str(self.longitude)
         gpsRMC["gpsRMC.EWIndicator"] = self.EW
         gpsRMC["gpsRMC.speedOverGround"] = self.speedOverGround
         gpsRMC["gpsRMC.courseOverGround"] = self.courseOverGround
         gpsRMC["gpsRMC.date"] = self.date
         gpsRMC["gpsRMC.mode"] = self.mode


      except ValueError:
         debug( "FAILED: invalid value")

#      print "Got here, GPRMC PASSED ! gpsRMC=", gpsRMC
      print (json.dumps(gpsRMC))
      print "\n"

      return True



   def process_gpgsa(self, in_line):
      print "$GPGSA record read ", in_line
      self.gsa = in_line.split(",")
      debug (self.gsa)

      # Sometimes multiple GPS data packets come into the stream. Take the data only after the last '$GPGSA' is seen
      try:
         ind=self.gsa.index('$GPGSA', 5, len(self.gsa))
         self.gsa=self.gsa[ind:]
      except ValueError:
         pass

      if len(self.gsa) != 18:
         debug ("Failed: wrong number of parameters ")
         debug (self.gsa)
         return False

#      for i in range(len(self.gsa)):
#         print "gsa[", i, "] = ", self.gsa[i]

      for i in range(len(self.validation_gpgsa)-1):
         if len(self.gsa[i]) == 0:
            debug ("Failed: empty string %d"%i)
            return False
         test = self.validation_gpgsa[i].match(self.gsa[i])
         if test == False:
            debug ("Failed: wrong format on parameter %d"%i)
            return False
         else:
            debug("Passed %d"%i)

      try:
         self.mode1 = self.gsa[1]
         self.mode2 = self.gsa[2]

         self.satelliteUsed01 = self.gsa[3]
         self.satelliteUsed02 = self.gsa[4]
         self.satelliteUsed03 = self.gsa[5]
         self.satelliteUsed04 = self.gsa[6]
         self.satelliteUsed05 = self.gsa[7]
         self.satelliteUsed06 = self.gsa[8]
         self.satelliteUsed07 = self.gsa[9]
         self.satelliteUsed08 = self.gsa[10]
         self.satelliteUsed09 = self.gsa[11]
         self.satelliteUsed10 = self.gsa[12]
         self.satelliteUsed11 = self.gsa[13]
         self.satelliteUsed12 = self.gsa[14]

         self.PDOP = float(self.gsa[15])
         self.HDOP = float(self.gsa[16])
         self.VDOP = float(self.gsa[17].split('*')[0])

         gpsGSA["gpsGSA.mode1"] = self.mode1
         gpsGSA["gpsGSA.mode2"] = self.mode2

         gpsGSA["gpsGSA.satelliteUsed01"] = self.satelliteUsed01
         gpsGSA["gpsGSA.satelliteUsed02"] = self.satelliteUsed02
         gpsGSA["gpsGSA.satelliteUsed03"] = self.satelliteUsed03
         gpsGSA["gpsGSA.satelliteUsed04"] = self.satelliteUsed04
         gpsGSA["gpsGSA.satelliteUsed05"] = self.satelliteUsed05
         gpsGSA["gpsGSA.satelliteUsed06"] = self.satelliteUsed06
         gpsGSA["gpsGSA.satelliteUsed07"] = self.satelliteUsed07
         gpsGSA["gpsGSA.satelliteUsed08"] = self.satelliteUsed08
         gpsGSA["gpsGSA.satelliteUsed09"] = self.satelliteUsed09
         gpsGSA["gpsGSA.satelliteUsed10"] = self.satelliteUsed10
         gpsGSA["gpsGSA.satelliteUsed11"] = self.satelliteUsed11
         gpsGSA["gpsGSA.satelliteUsed12"] = self.satelliteUsed12

         gpsGSA["gpsGSA.PDOP"] = self.PDOP
         gpsGSA["gpsGSA.HDOP"] = self.HDOP
         gpsGSA["gpsGSA.VDOP"] = self.VDOP

      except ValueError:
         debug( "FAILED: invalid value")

#      print "Got here, GPGSA PASSED ! gpsGSA=", gpsGSA
      print (json.dumps(gpsGSA))
      print "\n"

      return True


   def process_gpgga(self, in_line):
      print "$GPGGA record read ", in_line
      self.gga = in_line.split(",")
      debug (self.gga)

      # Sometimes multiple GPS data packets come into the stream. Take the data only after the last '$GPGGA' is seen
      try:
         ind=self.gga.index('$GPGGA', 5, len(self.gga))
         self.gga=self.gga[ind:]
      except ValueError:
         pass

      if len(self.gga) != 15:
         debug ("Failed: wrong number of parameters ")
         debug (self.gga)
         return False

      for i in range(len(self.validation_gpgga)-1):
         if len(self.gga[i]) == 0:
            debug ("Failed: empty string %d"%i)
            return False
         test = self.validation_gpgga[i].match(self.gga[i])
         if test == False:
            debug ("Failed: wrong format on parameter %d"%i)
            return False
         else:
            debug("Passed %d"%i)

      try:
         self.timestamp = self.gga[1]
         self.lat = float(self.gga[2])
         self.NS = self.gga[3]
         self.lon = float(self.gga[4])
         self.EW = self.gga[5]
         self.quality = int(self.gga[6])
         self.satellites = int(self.gga[7])
         self.altitude = float(self.gga[9])

         self.latitude = self.lat // 100 + self.lat % 100 / 60

         if self.NS == "S":
            self.latitude = - self.latitude

         self.longitude = self.lon // 100 + self.lon % 100 / 60

         if self.EW == "W":
            self.longitude = -self.longitude


         gpsGGAFixedData["gpsGGA.utcTime"] = self.timestamp
#         gpsGGAFixedData["gpsGGA.latitude"] = str(self.latitude)
         gpsGGAFixedData["gpsGGA.latitude"] = self.latitude
         gpsGGAFixedData["gpsGGA.NSIndicator"] = self.NS
#         gpsGGAFixedData["gpsGGA.Longitude"] = str(self.longitude)
         gpsGGAFixedData["gpsGGA.Longitude"] = self.longitude
         gpsGGAFixedData["gpsGGA.EWIndicator"] = self.EW
         gpsGGAFixedData["gpsGGA.positionFixIndicator"] = self.quality
         gpsGGAFixedData["gpsGGA.satellitesUsed"] = self.satellites
#         gpsGGAFixedData["gpsGGA.HDOP"] =self.gga[8]
         gpsGGAFixedData["gpsGGA.MSLAltitude.value"] = str(self.altitude)
         gpsGGAFixedData["gpsGGA.MSLAltitude.units"] = self.gga[10]
         gpsGGAFixedData["gpsGGA.geoidSeparation.value"] = self.gga[11]
         gpsGGAFixedData["gpsGGA.geoidSeparation.units"] = self.gga[12]
#         gpsGGAFixedData["gpsGGA.ageOfDiffCorr"] = self.gga[13]
         gpsGGAFixedData["gpsGGA.diffRefStationId"] = self.gga[14].split('*')[0]

         geoip2["lat"] = Decimal(str(self.latitude))
         geoip2["lon"] = Decimal(str(self.longitude))

#         geoip2["lat"] = Decimal(self.latitude)
#         geoip2["lon"] = Decimal(self.longitude)

#         geoip2["lat"] = str(self.latitude)
#         geoip2["lon"] = str(str(self.longitude))

#         gpsGGAFixedData["geo.coordinates"] = geoip2
#         gpsGGAFixedData["geoip.location"] = geoip3
#         gpsGGAFixedData["location"] = geoip4


      except ValueError:
         debug( "FAILED: invalid value")

      print (json.dumps(gpsGGAFixedData))
      print "\n"

      return True



if __name__ =="__main__":
    gps = usbGps("/dev/ttyUSB0", 4800, 0)
    while True:

      time.sleep(1)
      in_data = gps.read()
    if in_data != []:
#      print (in_data)
#      print "gpsGGAFixedData = " + json.dumps(gpsGGAFixedData)
        print "gpsGGAFixedData = ", gpsGGAFixedData
        print "geoip = " + json.dumps(geoip)
        print "geoip2 = ", geoip2


