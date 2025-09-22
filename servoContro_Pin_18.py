# my Second servo control app
# 24.04.2025 I am controling 1 9g Micro servo
# This time  I am going to control servos with 1 Rpi5 with GPIO 18
# I added 2 servoos with gpıo 12 and 18 at 02.05.2025 

# Initialize  the servo on GPIO pin 14
# min_pulse_width and max_pulse_width may need to be adjusted for you servo

from gpiozero import AngularServo
from time import sleep


servo2 = AngularServo(13,  min_pulse_width=0.5/1000 , max_pulse_width=2.500/1000)
servo1 = AngularServo(12,  min_pulse_width=500/1000000, max_pulse_width=2500/1000000)

while True:
    print("Moving to 0 (Min)")
    servo1.value =-1
    sleep(2)
    
    print("Moving servo 2 to 0 (Min)")
    servo2.value =-1
    sleep(2)
    
    
    print("Moving to 90 (Mid)")
    servo1.value=0
    sleep(2)
    
    print("Moving servo 2 to 90 (Mid)")
    servo2.value=0
    sleep(2)
    
    print("Moving to 0 (orta)")
    servo1.value =-0.5
    sleep(2)
    
    
    print("Moving to 180 (max)")
    servo1.value=1
    sleep(2)
    
    print("Moving to 0 (+ orta)")
    servo1.value =0.5
    sleep(2)


