import time
import RPi.GPIO as gpio
import paho.mqtt.client as mqtt

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(8, gpio.OUT)


def on_message(client, userdata, message):
    print ('Message arrived: ')
    print (message.payload.decode('utf-8'))	
    if str(message.payload.decode("utf-8")) == 'off':
	gpio.output(8,1)
    else:
	gpio.output(8,0)



broker_address="soldier.cloudmqtt.com"

client = mqtt.Client("P1") #create new instance
client.username_pw_set(username="yqglkysg",password="6upI7WF_DgVN")
client.on_message=on_message #attach function to callback
print("creating new instance")
print("connecting to broker")
client.connect(broker_address, port=17075) 
client.loop_start() 
print("Subscribing to topic","light/bulb1")
client.subscribe("light/bulb1")

time.sleep(400000) # wait
client.loop_stop() #stop the loop



