import RPi.GPIO as GPIO
import time, datetime
import paho.mqtt.client as paho
import SharedVar
import pygame.camera
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

broker="192.168.0.160"
port=1883

pir=7
SharedVar.buz=0
dateString = '%Y-%m-%d-%H-%M-%S'

def on_publish(client,userdata,result):
    print("data published \n")
pass


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir,GPIO.IN)
GPIO.setup(38,GPIO.OUT)

time.sleep(5) #SETTING UP THE SENSOR
print("SENSOR is READY")
while True:
	x=GPIO.input(pir)
	if x==1:
		if SharedVar.buz==0:
			GPIO.output(38,0)
			SharedVar.on()
			GPIO.output(5,0)
			client1= paho.Client("control1")                           
			client1.on_publish = on_publish                          
			client1.connect(broker,port)                             
			ret= client1.publish("house/fire","Fire")
			z= datetime.datetime.now().strftime(dateString)#STORING DATE AND TIME IN A VARIABLE
			pygame.init() #CAMERA SECTION
			pygame.camera.init()
			cam = pygame.camera.Camera("/dev/video0",(1280,720))
			cam.start()
			image= cam.get_image()
			pygame.image.save(image,'/home/pi/images/%s.jpg'%str(z))
			fromaddr = "aklc.contact@gmail.com" #EMAIL SECTION
			toaddr = "celestialcluster@gmail.com"
			msg = MIMEMultipart()
			msg['From'] = fromaddr
			msg['To'] = toaddr
			msg['Subject'] = "FILE ALARM ALERT"
			body = "PFA the attachment of the FILE ALARM at PIR1 @ "+str(z)
			msg.attach(MIMEText(body, 'plain'))
			filename = str(z)+".jpg"
			attachment = open('/home/pi/images/%s.jpg'%str(z), "rb")
			part = MIMEBase('application', 'octet-stream')
			part.set_payload((attachment).read())
			encoders.encode_base64(part)
			part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
			msg.attach(part)
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(fromaddr, "xxxxxxxxxxxxx")
			text = msg.as_string()
			server.sendmail(fromaddr, toaddr, text)
			server.quit()
			print 'Attachment sent'
			cam.stop()
	
	time.sleep(1)	
GPIO.cleanup()

