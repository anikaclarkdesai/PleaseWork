from gpiozero import Device, OutputDevice
from gpiozero.pins.lgpio import LGPIOFactory
import time

# Required for Raspberry Pi 5
Device.pin_factory = LGPIOFactory()


class Motor:
    def __init__(self, pin1, pin2):
        self._pin1 = pin1
        self._pin2 = pin2
        self._running = False
        self.pin1 = OutputDevice(pin1, active_high=True, initial_value=False)
        self.pin2 = OutputDevice(pin2, active_high=True, initial_value=False)
"""
    def clockwise(self):
        self.pin1.on()
        self.pin2.off()
        self._running = True

    def counterclockwise(self):
        self.pin1.off()
        self.pin2.on()
        self._running = True

    def stop(self):
        self.pin1.off()
        self.pin2.off()
        self._running = False   
        """
    def clockwise(self):
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)

    def counterclockwise(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)