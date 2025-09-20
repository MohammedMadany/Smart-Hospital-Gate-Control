from  gpiozero import InputDevice
from time import sleep

SOUND_PIN = 25

def is_siren_detected():
        sound = InputDevice(SOUND_PIN)
        if sound.is_active:
                return True
        return False

if __name__ == "__main__":
        while True:
                print(is_siren_detected())
                sleep(1)
