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

ADC = PCF8591(48)

class Joystick(PCF8591):
  
  def __init__(self):
    super().__init__(ADC)
    #self.address = PCF8591.address
    self.xch = 0x40
    self.ych = 0x41


  def getX(self):
    xvalue = PCF8591.read(self.xch)
    return xvalue
  
  def getY(self):
    yvalue = PCF8591.read(self.ych)
    return yvalue

MyJoy = Joystick()

print(MyJoy.getX(0x40), MyJoy.getY(0x41))
time.sleep(.1)
