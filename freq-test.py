import Adafruit_PCA9685
import time
# Create an instance of the PCA9685 class
pwm1 = Adafruit_PCA9685.PCA9685(0x40)
pwm2 = Adafruit_PCA9685.PCA9685(0x41)

# Set the PWM frequency to 50 Hz
pwm1.set_pwm_freq(120)
pwm2.set_pwm_freq(120)


while True:
    
    k,channel,frequency = input('enter servo k, channel, frequency: ').split()
    print(k,channel,frequency)
    if k=="1":
        pwm1.set_pwm(int(channel), 0, int(frequency))
    
    elif k == "2":
        pwm2.set_pwm(int(channel), 0,int(frequency))
        2
    elif k == "terminate":
        exit(1)
    else:
        print("wrong statement or not working: ")
