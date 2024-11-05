import RPi.GPIO as GPIO
import time

#Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 

#Use a variable for the Pin to use

led = 32
#Initialize your pin
GPIO.setup(led,GPIO.OUT)



#Blink loop
while True:
    #Turn on the LED
    print("LED on")
    GPIO.output(led,1)

    #Wait 3s
    time.sleep(3)

    #Turn off the LED
    print("LED off")
    GPIO.output(led,0)

    #Wait 5s
    time.sleep(3)