import machine
import utime

led = machine.PWM(machine.Pin(16))
pot = machine.ADC(26)


while True:
    #print(pot.read_u16())
    for i in range(0,pot.read_u16(),+100):
        utime.sleep_us(50)
        led.duty_u16(i)
    #print("increase",i)
    for i in range(pot.read_u16(),0,-100):
        utime.sleep_us(100)
        led.duty_u16(i)
        #print("decrease")
