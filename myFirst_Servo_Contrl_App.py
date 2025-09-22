# my first servo control app
# 24.04.2025 I am controling 1 9g Micro servo
# Next time I am going to control 2 servos with 1 Rpi5


# Initialize  the servo on GPIO pin 14
# min_pulse_width and max_pulse_width may need to be adjusted for you servo

from gpiozero import AngularServo
from time import sleep

servo = AngularServo(14, min_angle=0, max_angle=180, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

def set_angle(angle):
    servo.angle =angle
    sleep(1)
    
#main program loop
    
try:
    while True:
        angle = int(input("enter angle(0-180):")) # User input for angle
        set_angle(angle) #Set servo to entered angle
        
except KeyboardInterrupt:
    Print("Program stopped by User")
