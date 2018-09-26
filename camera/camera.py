import sys
import time
from threading import Timer
import math
import picamera
import datetime
from subprocess import call

imageFileDateFormat = "%Y%m%d%H%M%S-%f"
rootDirectory       = "/home/pi/Neil/project/"
imageDirectory      = rootDirectory + "images/"
videoDirectory      = rootDirectory + "video/"

class camera:

   def __init__(self):
      print("Initialising camera")
      self.camera = picamera.PiCamera()

#      self.camera.sharpness = 0
#      self.camera.contrast = 0
#      self.camera.brightness = 50
#      self.camera.saturation = 0
#      self.camera.ISO = 0
#      self.camera.video_stabilization = False
#      self.camera.exposure_compensation = 0
#      self.camera.exposure_mode = 'auto'
#      self.camera.meter_mode = 'average'
#      self.camera.awb_mode = 'auto'
#      self.camera.image_effect = 'none'
#      self.camera.color_effects = None
#      self.camera.rotation = 0
#      self.camera.hflip = False
#      self.camera.vflip = False
#      self.camera.crop = (0.0, 0.0, 1.0, 1.0)

   def __del__(self):
      print("destructor for camera")
      self.camera.close()

   def startPreview(self):
      print("start preview")
      self.camera.start_preview()
      return;

   def stopPreview(self):
      print("stop preview")
      self.camera.stop_preview()
      return;

   def startRecordingVideo(self, filename):
      video_format = "h264"
      self.videoOutputFilename = videoDirectory + filename + "." + video_format
      print("recording video to file", self.videoOutputFilename)

      self.camera.start_recording(self.videoOutputFilename, format=video_format)
      return;

   def startRecordingCurrentDateTime(self):
      now = datetime.datetime.now()
      filename = "video-" + now.strftime(imageFileDateFormat)
      print("using filename ", filename)
      self.startRecordingVideo(filename)
      return filename;

   def stopRecordingVideo(self):
      print("stopping recording video")
      self.camera.stop_recording()
      mp4Filename = self.videoOutputFilename + ".mp4"
      stdoutFilename = self.videoOutputFilename + ".txt"
      stdoutFD = open(stdoutFilename, 'w')
      print("converting captured file ", self.videoOutputFilename, " to MP4 file ", mp4Filename)
      call(["MP4Box", "-add", self.videoOutputFilename, mp4Filename], stdout=stdoutFD, stderr=stdoutFD)
      stdoutFD.close()

      return;

   def takePictureFile(self, filename):
      print("take picture to file", filename)
#      pictureFilename = imageDirectory + filename
#      self.camera.capture(pictureFilename)
      self.camera.capture(filename)
      return;

   def setOverlay(self, overlayText):
      print("setting overlay text >", overlayText, "<")
      self.camera.annotate_text = overlayText
      self.camera.annotate_background = picamera.Color('black')
      return;

   def clearOverlay(self):
      print("clearing overlay text")
      self.camera.annotate_text = ""
      return;

   def takePictureFileCurrentDateTime(self):
      now = datetime.datetime.now()
      dateTime = now.strftime(imageFileDateFormat)
      pictureFilename = imageDirectory + "image-" + dateTime + ".jpg"
#      self.setOverlay(dateTime)
      print("take picture to file", pictureFilename)
      self.camera.capture(pictureFilename)
      self.clearOverlay()
      return pictureFilename;

   def flipHorizontal(self):
      print("flipping horizontally")
      self.camera.hflip = True
      return;

   def unFlipHorizontal(self):
      print("unflipping vertically")
      self.camera.vflip = False
      return;

   def flipVertical(self):
      print("flipping vertically")
      self.camera.vflip = True
      return;

   def unFlipVertical(self):
      print("unflipping horizontally")
      self.camera.hflip = False
      return;

