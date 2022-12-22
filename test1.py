from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16, address=0x40, frequency=120)
kit1 = ServoKit(channels=16, address=0x41, frequency=120)
servo = 16

while True:
    a = input('enter servo angle: ')
    kit.servo[0].angle = int(a)
    kit1.servo[0].angle = int(a)




