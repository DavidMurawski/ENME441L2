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
  global address
  #def __init__(self, xch, ych):
   
  def getX(self, xch):
    xch = PCF8591.read(0x40)
    return xch
  
  def getY(self, ych):
    ych = PCF8591.read(0x41)
    return ych


print(Joystick.getX(), Joystick.getY())
time.sleep(.1)