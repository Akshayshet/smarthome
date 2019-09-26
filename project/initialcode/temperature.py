import pigpio
import DHT22
import RPi.GPIO as gpio

from time import sleep
import paho.mqtt.client as paho
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(36, gpio.OUT)
gpio.setup(38, gpio.OUT)


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
    if temp > 30:
       gpio.output(36,1)
       gpio.output(38,0)
    else:
       gpio.output(36,0)
       gpio.output(38,1)
    client1= paho.Client("control1")   
    client1.username_pw_set(username="yqglkysg",password="6upI7WF_DgVN")                        
    client1.on_publish = on_publish                          
    client1.connect(broker,port)                             
    ret= client1.publish("house/temp", "Temperature : "+temp+" degC"+", "+"Humidity : "+humidity+"%")

    sleep(sleepTime)
