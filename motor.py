#import RPi.GPIO
#import RpiMotorLib
import time


#motor_run_zero = RpiMotorLib.A4988Nema(22, 23, (21,21,21), "DRV8825")
#motor_run_one = RpiMotorLib.A4988Nema(17, 23, (21,21,21), "DRV8825")
#RPi.GPIO.setup(24,RPi.GPIO.OUT)

def motorR(distance, direction):
    RPi.GPIO.output(enable,RPi.GPIO.LOW)
    motor_run_zero.motor_go(direction[0], "Full", distance, 0.005, False, .0)

def motorL(distance, direction):
    RPi.GPIO.output(enable,RPi.GPIO.LOW)
    motor_run_one.motor_go(direction[1], "Full", distance, 0.005, False, .0)

   
