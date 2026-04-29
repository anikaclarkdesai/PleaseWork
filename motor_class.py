from gpiozero import Device, OutputDevice
from gpiozero.pins.lgpio import LGPIOFactory

# Required for Raspberry Pi 5
Device.pin_factory = LGPIOFactory()


class Motor:
    def __init__(self, pin1, pin2):
        self.pin1 = OutputDevice(pin1, active_high=True, initial_value=False)
        self.pin2 = OutputDevice(pin2, active_high=True, initial_value=False)

    def clockwise(self):
        self.pin1.on()
        self.pin2.off()

    def counterclockwise(self):
        self.pin1.off()
        self.pin2.on()

    def stop(self):
        self.pin1.off()
        self.pin2.off()