import RPi.GPIO as GPIO
import time, datetime
import paho.mqtt.client as paho

pir = 7
broker="soldier.cloudmqtt.com"
port=16444
x = 0
state = 'on'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(pir,GPIO.IN)

def on_message(client, userdata, message):
	global x
	global state
    	print ('Message arrived: ')
    	print (message.payload.decode('utf-8'))
	state = message.payload.decode('utf-8').lower()
	if state == 'off':
		x = 1
	else:
		x = 0

def on_publish(client,userdata,result):
   print("data published \n")
pass

def fireOn():
	global state
	if state == 'off':
		GPIO.output(38,1)
	else:
		GPIO.output(38,0)

time.sleep(5) #SETTING UP THE SENSOR
print("SENSOR is READY")
while True:
	x = GPIO.input(pir)
	print(x)
	client1= paho.Client("control1")
	client1.on_message=on_message
	client1.username_pw_set(username="foszubbs",password="K-FHc0ewoEWL")
	client1.connect(broker,port)
	client1.on_publish = on_publish
	client1.subscribe("fire/control")
	client1.loop_start()
	time.sleep(1)
	if x == 0:
		fireOn()
		time.sleep(5)
	else:
		fireOn()
		time.sleep(5)
	client1.loop_stop()  
	client1.disconnect()