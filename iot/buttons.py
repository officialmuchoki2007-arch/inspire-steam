from machine import Pin



import time

import machine


red_led =  Pin(28, Pin.OUT)

yellow_led =  Pin(27, Pin.OUT)

# Button is input
green_btn = Pin(22, Pin.IN, Pin.PULL_UP)

while True:
    button_status = green_btn.value()
    if (button_status == 1):
        red_led.off()
        print("button released")

    elif  (button_status == 0):
        red_led.on()
        print("button pressed")

    time.sleep(1)

