import RPi.GPIO as GPIO
import time, datetime
import paho.mqtt.client as paho

broker="soldier.cloudmqtt.com"
port=17205

pir=7

def on_publish(client,userdata,result):
    print("data published \n")
pass


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir,GPIO.IN)


time.sleep(5) #SETTING UP THE SENSOR
print("SENSOR is READY")
while True:
	x=GPIO.input(pir)
	print(x)
	if x==0:
		client1= paho.Client("control1")                           
		client1.username_pw_set(username="aknqmvgn",password="Bnv14sNdag_l")
		client1.on_publish = on_publish                          
		client1.connect(broker,port)                             
		ret= client1.publish("house/fire","Fire")
	else:
		client1= paho.Client("control1")                           
		client1.username_pw_set(username="aknqmvgn",password="Bnv14sNdag_l")
		client1.on_publish = on_publish                          
		client1.connect(broker,port)                             
		ret= client1.publish("house/fire","No Fire")		
	time.sleep(1)	
GPIO.cleanup()

