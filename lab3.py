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

class Joystick:
  def __init__(self, bus, address, xch, ych):
    self.xch = 0x40
    self.ych = 0x41
    self.bus = smbus.SMBus(1)
    self.address = address
  
  def getX(self, xch):
    try:
      self.PCF8591.read(xch)
    except Exception as e:
      print ("Error: Device address: 0x%2X \n%s" % (self.address,e))
    return self.PCF8591.read(xch)

  #def getY(self, ):

TheJoystick = Joystick(1)

print(Joystick.getX())
time.sleep(.1)