from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16, address=0x40, frequency=120)
kit1 = ServoKit(channels=16, address=0x41, frequency=50)

servo = 16

while True:
    kit1.servo[0].angle = 150
    kit1.servo[1].angle = 180
    sleep(1)

    kit1.servo[0].angle = 50
    kit1.servo[1].angle = 50
    sleep(1)




