from gpiozero import Servo
from time import sleep
import BlynkLib

BLYNK_TEMPLATE_NAME = "ultrasonic"
BLYNK_ULTRA = "h9XeEbrLO8iuF_16vwmn-QwP9Z_sckyZ"
blynk = BlynkLib.Blynk(BLYNK_ULTRA, server="blynk.cloud", port=80)
SERVO_PIN = 18
servo = Servo(SERVO_PIN)

def open_gate(emergency=False):
        speed = 0.01 if emergency else 0.05

        for i in range(0, 90, 5):
                servo.value = i / 90.0 - 1
                sleep(speed)

def close_gate(emergency=False):
        speed = 0.01 if emergency else 0.05
        for i in range(90, 0, -5):
                servo.value = i / 90.0 - 1
                sleep(speed)

def v0_write(value):
        if int(value[0]) != 0:
                open_gate()
        else:
                close_gate()
blynk.on('V0',v0_write)

if __name__ == "__main__":
        while 1:
                blynk.run()
