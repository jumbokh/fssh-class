import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)

while True: 
    led_onboard.value(1) 
    utime.sleep(5) 
    led_onboard.value(0) 
    utime.sleep(5)