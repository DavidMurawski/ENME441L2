import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

in1, in2, out1, out2, out3 = 17, 27, 13, 19, 26

GPIO.setup(in1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(out1, GPIO.OUT, initial=0)
GPIO.setup(out2, GPIO.OUT, initial=0)
GPIO.setup(out3, GPIO.OUT, initial=0)

dc1 = 50
f1 = 1
pwm0 = GPIO.PWM(out1, f1)
pwm1 = GPIO.PWM(out2, f1)
pwm2 = GPIO.PWM(out3, f1)

pwm0.start(dc1)

def myCallback(pin):
    print("Rising edge detected on pin %d" % pin)
    if pin == in1:
      try:
        pwm1.start(dc1)
        while True:
          for dc in range(101):
            pwm1.ChangeDutyCycle(dc)
            time.sleep(0.01)
          for dc in range(100,1,1):
            pwm1.ChangeDutyCycle(dc)
            time.sleep(0.01)
      except KeyboardInterrupt:
        print('\nExiting')
        GPIO.cleanup()
    if pin == in2:
      try:
        pwm2.start(dc1)
        while True:
          for dc in range(101):
            pwm2.ChangeDutyCycle(dc)
            time.sleep(0.01)
          for dc in range(100,1,1):
            pwm2.ChangeDutyCycle(dc)
            time.sleep(0.01)
      except KeyboardInterrupt:
        print('\nExiting')
        GPIO.cleanup()        

GPIO.add_event_detect(in1, GPIO.RISING, callback=myCallback, bouncetime=100)

GPIO.add_event_detect(in2, GPIO.RISING, callback=myCallback, bouncetime=100)

while True:
  print(".")
  time.sleep(0.1)

pwm0.stop()
pwm1.stop()
pwm2.stop()
GPIO.cleanup()