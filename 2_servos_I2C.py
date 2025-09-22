"""
25.07.2025 denendi



source ~/pca_env/bin/activate
pip install lgpi

python

copy-paste codes below
 

https://copilot.microsoft.com/shares/bCAXhVMRjFhX7EVtTHawV


"""



import time
import board
import busio
from adafruit_pca9685 import PCA9685

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

# Create a PCA9685 instance and set frequency to 50Hz for servos
pca = PCA9685(i2c)
pca.frequency = 50

# Function to convert angle (0–180°) to duty cycle value
def angle_to_duty(angle):
    min_duty = 1600   # adjust based on your servo's specs
    max_duty = 6500
    duty_span = max_duty - min_duty
    return int(min_duty + (angle / 180.0) * duty_span)

# Servo channel (0–15 on PCA9685)
servo_channel = 0
servo1_channel = 1
# Sweep servo from 0° to 180°, then back
try:
    while True:
        for angle in range(0, 181, 20):
            duty = angle_to_duty(angle)
            pca.channels[servo_channel].duty_cycle = duty
            pca.channels[servo1_channel].duty_cycle = duty
            print(f"Angle: {angle}°, Duty: {duty}")
            time.sleep(3)     
        for angle in range(180, -1, -20):
            duty = angle_to_duty(angle)
            pca.channels[servo_channel].duty_cycle = duty
            pca.channels[servo1_channel].duty_cycle = duty
            print(f"Angle: {angle}°, Duty: {duty}")
            time.sleep(3)
except KeyboardInterrupt:
    print("Stopping servo sweep.")

# Cleanup
pca.deinit()
