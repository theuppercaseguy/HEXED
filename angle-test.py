from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16, address=0x40, frequency=120)
kit1 = ServoKit(channels=16, address=0x41, frequency=120)

servo = 16

while True:
    k,channel,degree = input('enter servo k, channel, degree: ').split()
    print(k,channel,degree)
    if k=="1":
            kit.servo[int(channel)].angle = int(degree)
    elif k == "2":
            kit1.servo[int(channel)].angle = int(degree)
    if k == "terminate":
        exit(1)
    else:
        print("wrong statement or not working: ")
    





