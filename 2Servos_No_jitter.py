import RPi.GPIO as GPIO
import time

#set up GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

#set up PWM on the pins

pwm1= GPIO.PWM(11,50) # 50 herz frequency
pwm2= GPIO.PWM(13,50) # 50 herz frequency

#start PWM with 0 duty cycle (servos off)

pwm1.start(0)
pwm2.start(0)

def set_angle(pwm,angle):
    duty = angle/ 18 +2
    GPIO.output(11,True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(11,False)
    pwm.ChangeDutyCycle(0)
    
    
try:
    while True:
        #Example : Moveservos to 90 degrees
        set_angle(pwm1,90)
        set_angle(pwm2,90)
        time.sleep(2)
        
        #Move servos to 0  degrees
        set_angle(pwm1,0)
        set_angle(pwm2,0)
        time.sleep(2)
        
except KeyboardInterrupt:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()
