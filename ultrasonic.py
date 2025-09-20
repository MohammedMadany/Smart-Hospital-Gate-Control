from gpiozero import DistanceSensor
import BlynkLib
from time import sleep

BLYNK_TEMPLATE_NAME = "ultrasonic"
BLYNK_ULTRA = "x84GYfzJkF1S-DgI8JYZ5PSG-RKZODTX"
blynk = BlynkLib.Blynk(BLYNK_ULTRA, server="blynk.cloud", port=80)
ultra = DistanceSensor(echo=17,trigger=4)

def get_distance():
    distance = ultra.distance * 100
    blynk.virtual_write(1,distance)
    print(distance)
    return distance


if __name__ == "__main__":
    while 1:
        blynk.run()
        get_distance()
        sleep(1)
