import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time


broker_address="192.168.43.99"
port=1883
def on_publish(client,userdata,result):
    print("data published \n")
pass

def on_message(client, userdata, message):
    print ("Got message {} ".format(message.payload))
    if message.payload == "on":
        GPIO.output(4,GPIO.LOW)
    else:
        GPIO.output(4,GPIO.HIGH)



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,GPIO.LOW)
print "LED on"
time.sleep(2)
GPIO.output(4,GPIO.HIGH)
print "LED off"

client = mqtt.Client("bulb1") #create new instance

client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address) 
client.loop_start() 
print("Subscribing to topic","house/bulb1")
client.subscribe("house/bulb1")

time.sleep(400000) # wait
client.loop_stop() #stop the loop