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
f1 = 10000
pwm0 = GPIO.PWM(out1, 1)
pwm1 = GPIO.PWM(out2, f1)
pwm2 = GPIO.PWM(out3, f1)

pwm1.start(100)
pwm2.start(100)

def myCallback(pin):
    print("Rising edge detected on pin %d" % pin)
    try:
      if GPIO.input(in1) == GPIO.HIGH:
        pwm1.start(100)
        for dc in range(100,0,-1):
          pwm1.ChangeDutyCycle(dc)
          time.sleep(0.01)        
        for dc in range(0,100,1):
          pwm1.ChangeDutyCycle(dc)
          time.sleep(0.01)
        pwm1.ChangeDutyCycle(100)
      if GPIO.input(in2) == GPIO.HIGH:
        pwm2.start(100)
        for dc in range(100,0,-1):
          pwm2.ChangeDutyCycle(dc)
          time.sleep(0.01)        
        for dc in range(0,100,1):
          pwm2.ChangeDutyCycle(dc)
          time.sleep(0.01)
        pwm2.ChangeDutyCycle(100)
    except KeyboardInterrupt:
      print('\nExiting')
      GPIO.cleanup()      

GPIO.add_event_detect(in1, GPIO.RISING, callback=myCallback, bouncetime=100)

GPIO.add_event_detect(in2, GPIO.RISING, callback=myCallback, bouncetime=100)

while True:
  try:
    pwm0.start(dc1)
  except KeyboardInterrupt:
    GPIO.cleanup()

