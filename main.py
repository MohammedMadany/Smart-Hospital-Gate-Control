import time
from ultrasonic import get_distance
from servo import open_gate, close_gate
#from camera_detection import is_ambulance
from sound_sensor import is_siren_detected
from lcd import display_status


def main():
        while True:
                distance = get_distance()
                display_status(f"Dist: {distance} cm")

                emergency = False
                if distance < 10:
#                       if is_ambulance or is_siren_detected:
#                               emergency = True
                        open_gate(emergency)
                        time.sleep(2)
                        close_gate()
                time.sleep(2)


main()
