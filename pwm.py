import machine
import utime

led = machine.PWM(machine.Pin(25))
while True:
    #led.duty_u16(10000)
    led.duty_u16(100)
    utime.sleep(0.2)
    led.duty_u16(200)
    utime.sleep(0.2)
    led.duty_u16(300)
    utime.sleep(0.2)
    led.duty_u16(400)
    utime.sleep(0.2)
    led.duty_u16(500)
    utime.sleep(0.2)
    led.duty_u16(600)
    utime.sleep(0.2)
    led.duty_u16(700)
    utime.sleep(0.2)
    led.duty_u16(800)
    utime.sleep(0.2)
    led.duty_u16(900)
    utime.sleep(0.2)
    led.duty_u16(1000)
    utime.sleep(0.2)
    led.duty_u16(2000)
    utime.sleep(0.2)
    led.duty_u16(3000)
    utime.sleep(0.2)
    led.duty_u16(4000)
    utime.sleep(0.2)
    led.duty_u16(5000)
    utime.sleep(0.2)
    led.duty_u16(6000)
    utime.sleep(0.2)
    led.duty_u16(7000)
    utime.sleep(0.2)
    led.duty_u16(8000)
    utime.sleep(0.2)
    led.duty_u16(9000)
    utime.sleep(0.2)
    led.duty_u16(10000)
    utime.sleep(0.2)
    led.duty_u16(20000)
    utime.sleep(0.2)
    led.duty_u16(30000)
    utime.sleep(0.2)
    led.duty_u16(40000)
    utime.sleep(0.2)
    led.duty_u16(50000)
    utime.sleep(0.2)
    led.duty_u16(60000)