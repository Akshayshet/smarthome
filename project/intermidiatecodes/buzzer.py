import time
import RPi.GPIO as gpio
import paho.mqtt.client as mqtt #import the client1
import SharedVar

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(5,gpio.OUT)
gpio.setup(38,gpio.OUT)

def on_message(client, userdata, message):
    SharedVar.off()
    gpio.output(38,1)
    gpio.output(5,1)



broker_address="192.168.0.160"

print("creating new instance")
client = mqtt.Client("P1") #create new instance

client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address) 
client.loop_start() 
print("Subscribing to topic","house/alarm")
client.subscribe("house/alarm")

time.sleep(400000) # wait
client.loop_stop() #stop the loop