import RPi.GPIO as GPIO

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)

pwm_led = GPIO.PWM(led_pin,50)
pwm_led.start(100)

while (True):
    duty_s = raw_input("Enter brightness 0-100")
    duty = int(duty_s)
    pwm_led.ChangeDutyCycle(duty)
 
