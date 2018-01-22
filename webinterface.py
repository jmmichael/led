'''http://apprize.info/hardware/raspberry/10.html
Ran with web error, possibly because another web server was running?
'''
from bottle import route, run

import RPi.GPIO as GPIO

host = '192.168.1.99'

GPIO.setmode(GPIO.BOARD)

led_pins = [16, 18, 36]

led_states = [0, 0, 0]

switch_pin = 22

GPIO.setup(led_pins[0], GPIO.OUT)

GPIO.setup(led_pins[1], GPIO.OUT)

GPIO.setup(led_pins[2], GPIO.OUT)

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def switch_status():

    state = GPIO.input(switch_pin)

    if state:

        return 'Up'

    else:

        return 'Down'

def html_for_led(led):

    l = str(led)

    result = " <input type='button' onClick='changed(" + l + ")"

    value='LED " + l + "/>'

    return result

def update_leds():

    for i, value in enumerate(led_states):

        GPIO.output(led_pins[i], value)

@route('/')

@route('/<led>')

def index(led="n"):

    if led != "n":

        led_num = int(led)

        led_states[led_num] = notled_states[led_num]

        update_leds()

    response = "<script>"

    response += "function changed(led)"

    response += "{"

    response += "  window.location.href='/' + led"

    response += "}"

    response += "</script>"

    response += '<h1>GPIO Control</h1>'

    response += '<h2>Button=' + switch_status() + '</h2>'

    response += '<h2>LEDs</h2>'

    response += html_for_led(0)

    response += html_for_led(1)

    response += html_for_led(2)

    return response

run(host=host, port=80)

