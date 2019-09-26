import time
import RPi.GPIO as gpio
import paho.mqtt.client as mqtt
state = "off"
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(8, gpio.OUT)
def on_message(client, userdata, message):
    global state
    print ('Message arrived: ')
    print (message.payload.decode('utf-8'))
    state = message.payload.decode('utf-8')
def blink():
    gpio.output(8,0)
    time.sleep(2)
    gpio.output(8,1)
    time.sleep(2)
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
while True:
    if state == 'on':
        gpio.output(8,0)
    elif state == 'blink':
        blink()
    else:
        gpio.output(8,1)
time.sleep(400000) # wait
client.loop_stop() #stop the loop