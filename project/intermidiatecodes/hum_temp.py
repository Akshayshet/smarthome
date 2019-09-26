import pigpio
import DHT22
from time import sleep
import paho.mqtt.client as paho
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(40,gpio.OUT)


broker="192.168.0.160"
port=1883
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
    if float(temp)>31:
		gpio.output(40,0)
    else:
		gpio.output(40,1)

    client1= paho.Client("temp_humidity")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)                             
    ret= client1.publish("house/room",temp+"C,"+humidity+"%")
    sleep(sleepTime)
