import machine
import utime

led = machine.PWM(machine.Pin(25))

while True:
    for i in range(65400):
        utime.sleep_us(1)
        led.duty_u16(i)
        utime.sleep_us(1)
