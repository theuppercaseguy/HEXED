from Adafruit_PCA9685 import PCA9685
import time
# Create an instance of the PCA9685 class
pwm = PCA9685()

# Set the PWM frequency to 50 Hz
pwm.set_pwm_freq(50)

while True:
    # Set the servo to the minimum position (fully counterclockwise)
    pwm.set_pwm(0, 0, 0)
    time.sleep(1)

    # Set the servo to the maximum position (fully clockwise)
    pwm.set_pwm(0, 0, 0)
    time.sleep(1)
