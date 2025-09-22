from gpiozero import AngularServo
from time import sleep

import time
from picamera2 import Picamera2, Preview

picam = Picamera2()

config = picam.create_preview_configuration()
picam.configure(config)

picam.start_preview(Preview.QTGL)


picam.start()
time.sleep(2)
#picam.capture_file("test-python.jpg")

#picam.close()




servo2 = AngularServo(13, min_angle=0,max_angle=180, min_pulse_width=0.5/1000, max_pulse_width=3.00/1000)
servo1 = AngularServo(12,  min_pulse_width=500/1000000, max_pulse_width=2500/1000000)
#servo2 = AngularServo(13, min_angle=0,max_angle=180, min_pulse_width=0.5/1000 , max_pulse_width=2.500/1000)
while True:
    
    for i in range(0,21,2):
        
        setted_value = (i-10)/10
        print("Moving to 0 (Min)",setted_value)
        servo2.value = setted_value
        picam.capture_file(str(i)+".jpg")
        sleep(0.2)
    sleep(60)
    
   

