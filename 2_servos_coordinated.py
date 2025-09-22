from gpiozero import AngularServo
from time import sleep


servo2 = AngularServo(13, min_angle=0,max_angle=180, min_pulse_width=0.5/1000, max_pulse_width=3.00/1000)
servo1 = AngularServo(12,  min_pulse_width=500/1000000, max_pulse_width=2500/1000000)
#servo2 = AngularServo(13, min_angle=0,max_angle=180, min_pulse_width=0.5/1000 , max_pulse_width=2.500/1000)
while True:
    
    for i in range(0,21,2):
        
        setted_value = (i-10)/10
        print("Moving to 0 (Min)",setted_value)
        servo2.value = setted_value
        sleep(0.2)
        for j in range(0,16,2):
        
            setted_value = (j-10)/10
            print("Moving to 0 (Min)",setted_value)
            servo1.value = setted_value
            sleep(0.2)
    
