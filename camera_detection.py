from picamera2 import Picamera2
from ultralytics import YOLO
import cv2
import random

model = YOLO("yolov8s.pt")

def is_ambulance():
        picam2 = Picamera2()
        picam2.start()
        image = picam2.capture_array()
        picam2.stop()

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        results = model(image)

        for r in results:
                if "trunk" in r.names:
                        return True

        return random.choice([True, False])
