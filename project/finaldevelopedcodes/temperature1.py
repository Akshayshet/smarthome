import pigpio
import DHT22
import RPi.GPIO as GPIO
from time import sleep
import paho.mqtt.client as paho


broker="soldier.cloudmqtt.com"
port=17075

def on_publish(client,userdata,result):
    print("data published \n")
pass



pi = pigpio.pi()
dht22 = DHT22.sensor(pi,14)

dht22.trigger() # scrap the first reading
sleepTime = 3 # Dont read temp more than once every 2 seconds 

def readDHT22():
    dht22.trigger()
    humidity = '%.2f' % (dht22.humidity())
    temp = '%.2f' % (dht22.temperature())
    return (humidity, temp)

while True:
    humidity, temp = readDHT22()
    print("Humidity : "+humidity+"%")
    print("Temperature : "+temp+"C")
    client1= paho.Client("control1")   
    client1.username_pw_set(username="yqglkysg",password="6upI7WF_DgVN")                        
    client1.on_publish = on_publish                          
    client1.connect(broker,port)                             
    ret= client1.publish("house/temp", "Temperature : "+temp+" degC"+", "+"Humidity : "+humidity+"%")

    sleep(sleepTime)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(21,GPIO.OUT) #RGB blue
GPIO.output(21,GPIO.LOW)
GPIO.setup(40,GPIO.OUT) #RGB red
GPIO.output(40,GPIO.LOW)

if temperature > 30:
    GPIO.output(21,GPIO.HIGH)
if temperature < 37:
    GPIO.output(40,GPIO.HIGH)
    
GPIO.cleanup()
