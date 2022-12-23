import Adafruit_PCA9685
import time
# Create an instance of the PCA9685 class
pwm1 = Adafruit_PCA9685.PCA9685(0x40)
pwm2 = Adafruit_PCA9685.PCA9685(0x41)

# Set the PWM frequency to 50 Hz
pwm1.set_pwm_freq(120)
pwm2.set_pwm_freq(120)

def set_servo_pulse(k,channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length

    if k == 1:
        pwm1.set_pwm(channel, 0, pulse)
    elif k == 2:
        pwm2.set_pwm(channel, 0, pulse)



while True:
    
    k,channel,frequency = input('enter servo k, channel, frequency: ').split()
    print(k,channel,frequency)
    if k=="1":
            set_servo_pulse(int(k),int(channel),int(frequency))

    elif k == "2":
            set_servo_pulse(int(k),int(channel),int(frequency))    

    elif k == "terminate":
        exit(1)
    else:
        print("wrong statement or not working: ")
