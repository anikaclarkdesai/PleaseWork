from motor_class import Motor
import time

# BCM pins
motor1 = Motor(16, 18)

print("Clockwise")
motor1.clockwise()
time.sleep(7)

print("Counterclockwise")
motor1.counterclockwise()
time.sleep(5)

print("Clockwise again")
motor1.clockwise()
time.sleep(10)

print("Stopping")
motor1.stop()
