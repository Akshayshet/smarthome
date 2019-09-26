import pigpio
import DHT22
from time import sleep
import paho.mqtt.client as paho
broker="192.168.0.160"
port=1883
def on_publish(client,userdata,result):
    print("data published \n")
pass

pi = pigpio.pi()
dht22 = DHT22.sensor(pi,8)

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
    client1.on_publish = on_publish                          
    client1.connect(broker,port)                             
    ret= client1.publish("dev/temp", "Humidity : "+humidity+"%"+", "+"Temperature : "+temp+"C")

    sleep(sleepTime)
