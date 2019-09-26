import RPi.GPIO as GPIO     # importing GPIO library
import time                 # importing time library for delay

GPIO.setmode(GPIO.BOARD)     # enable BOARD pin numberings
GPIO.setup(8,GPIO.OUT)      # Set pin 11 as output

GPIO.output(8,1)            # Send Output 5V to pin 11
time.sleep(1)                # introduce 1 second time delay before executing next line of code
                             
GPIO.output(8,0)            # Send Output 0V to pin 11
time.sleep(1)                # introduce 1 second time delay

GPIO.output(8,1)            # Send Output 5V to pin 11
time.sleep(1)                # introduce 1 second time delay

GPIO.output(8,0)            # Send Output 0V to pin 11
time.sleep(1)                # introduce 1 second time delay

GPIO.output(8,1)            # Send Output 5V to pin 11
time.sleep(1)                # introduce 1 second time delay

GPIO.cleanup()   