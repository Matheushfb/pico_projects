import machine
import utime
led = machine.Pin(25, machine.Pin.OUT)
while True:
    led(1)
    utime.sleep(1)
    led(0)
    utime.sleep(1)
    
 