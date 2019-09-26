import RPi.GPIO as GPIO
import time, datetime
import paho.mqtt.client as paho
broker="soldier.cloudmqtt.com"
port=17075
pir=7
def on_publish(client,userdata,result):
    print("data published \n")
pass
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir,GPIO.IN)
def on_message(client, userdata, message):
    print ('Message arrived: ')
    print (message.payload.decode('utf-8'))=='off'
    if str(message.payload.decode("utf-8")) == 'off':
	gpio.output(5,1)
    else:
	gpio.output(5,0)

time.sleep(5) #SETTING UP THE SENSOR
print("SENSOR is READY")
while True:
	x=GPIO.input(pir)
	print(x)
	if x==0:
		GPIO.output(5,0)
		client1= paho.Client("control1")
		client1.connect(broker,port)                       
		client1.username_pw_set(username="yqglkysg",password="6upI7WF_DgVN")
		client1.subscribe("house/fire")
		client1.on_publish = on_publish                           
		ret= client1.publish("house/fire","Fire")
	else:
		client1= paho.Client("control1")                           
		client1.username_pw_set(username="yqglkysg",password="6upI7WF_DgVN")
		client1.on_publish = on_publish                          
		client1.connect(broker,port)                             
		ret= client1.publish("house/fire","No Fire")		
	time.sleep(1)	
GPIO.cleanup()