import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

in1, in2, out1, out2, out3 = 17, 27, 13, 19, 26

GPIO.setup(in1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(out1, GPIO.OUT, initial=0)
GPIO.setup(out2, GPIO.OUT, initial=0)
GPIO.setup(out3, GPIO.OUT, initial=0)


def myCallback(pin):
    print("Rising edge detected on pin %d" % pin)

GPIO.add_event_detect(in1, GPIO.RISING, callback=myCallback, bouncetime=100)


GPIO.cleanup()