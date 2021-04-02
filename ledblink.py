import machine
import utime
led = machine.Pin(25, machine.Pin.OUT)
pot = machine.ADC(26)


while True:
    led(1)
    utime.sleep(1)
    led(0)
    utime.sleep(1)
    print(pot.read_u16())
    
 