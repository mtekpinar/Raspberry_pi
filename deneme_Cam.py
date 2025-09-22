
from ai_camera import IMX500Detector
import time

camera = IMX500Detector()

# Start the detector with preview window
camera.start(show_preview=True)


# Main loop
while True:
    # Get the latest detections
    detections = camera.get_detections()
    
    # Get the labels for reference
    labels = camera.get_labels()
