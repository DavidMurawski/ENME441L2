import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

in1, in2, out1, out2, out3 = 17, 27, 13, 19, 26

GPIO.setup(in1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(out1, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(out3, GPIO.OUT)

dc1 = 50
f1 = 100
pwm1 = GPIO.PWM(out2, f1)
pwm2 = GPIO.PWM(out3, f1)

pwm1.start(100)
pwm2.start(100)

def myCallback(pin):
    print("Rising edge detected on pin %d" % pin)
    try:
      if GPIO.input(in1) == 1:
        pwm1.start(100)
        for dc in range(100,0,-1):
          pwm1.ChangeDutyCycle(dc)
          time.sleep(0.01)
          print("1 going up")        
        for dc in range(0,101,1):
          pwm1.ChangeDutyCycle(dc)
          time.sleep(0.01)
          print("1 going down")
      if GPIO.input(in2) == 1:
        pwm2.start(100)
        for dc in range(100,0,-1):
          pwm2.ChangeDutyCycle(dc)
          time.sleep(0.01)        
        for dc in range(0,101,1):
          pwm2.ChangeDutyCycle(dc)
          time.sleep(0.01)
    except KeyboardInterrupt:
      print('\nExiting') 

GPIO.add_event_detect(in1, GPIO.RISING, callback=myCallback, bouncetime=300)

GPIO.add_event_detect(in2, GPIO.RISING, callback=myCallback, bouncetime=300)

while True:
  GPIO.output(out1,0)
  time.sleep(.5)
  GPIO.output(out1,1)
  time.sleep(.5)

pwm1.stop()
pwm2.stop()
GPIO.output(out1,1)
GPIO.output(out2,1)
GPIO.output(out3,1)
GPIO.cleanup()