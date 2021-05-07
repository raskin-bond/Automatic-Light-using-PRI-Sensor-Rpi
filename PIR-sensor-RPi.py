import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(25, GPIO.OUT)         #LED output pin


x = 1
y = 1
while True:

  i=GPIO.input(17)
  
  
  
  
  if i==1:               #When output from motion sensor is HIGH
    print ("Intruder Detected",i)
    GPIO.output(25, GPIO.LOW)#Turn ON LED
    x=1
    time.sleep(1)
  if i==0:                 #When output from motion sensor is LOW
    
    x += 1
    print(x)
    time.sleep(2)
    
  if x >=10:
    print ("Intruders not Detected",i)
    GPIO.output(25, GPIO.HIGH)  #Turn OFF LED
    time.sleep(1)
    
GPIO.cleanup()
