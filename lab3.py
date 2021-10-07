#David Murawski, ENME441 Lab 3 10/07/21
#   To check address: sudo i2cdetect -y 1

import smbus
import time

class PCF8591:
  
  def __init__(self,address):
    self.bus = smbus.SMBus(1)
    self.address = address

  def read(self,chn): #channel
      try:
          self.bus.write_byte(self.address, 0x40 | chn)  # 01000000
          self.bus.read_byte(self.address) # dummy read to start conversion
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)

  def write(self,val):
      try:
          self.bus.write_byte_data(self.address, 0x40, int(val))
      except Exception as e:
          print ("Error: Device address: 0x%2X \n%s" % (self.address,e))

#Create a new class for the Joystick with PCF8591 included
class Joystick(PCF8591):
  #instantiate and pull in address from PCF8591
  def __init__(self, address):
      super().__init__(address)

  #Define a method for getting the x value and read from channel 0
  def getX(self):
      return super().read(0)
  #Define a method for getting the y value and read from channel 1
  def getY(self):
      return super().read(1)

#Create a Joystick object named "MyJoy"
MyJoy = Joystick(0x48)

#Call and print the Joystick values every .1 seconds, and allow for a keyboard interrupt to stop
while True:
  try:
    print(str(MyJoy.getX()) + ", " + str(MyJoy.getY()))
    time.sleep(.1)
  except KeyboardInterrupt:
    print("Stopping")
    break