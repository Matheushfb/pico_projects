import machine
import utime

led = machine.PWM(machine.Pin(16))
pot = machine.ADC(26


while True:
    print(potentiometer.read_u16())
    #for i in range(0,65635,+100):
    #    utime.sleep_us(5)
    #    led.duty_u16(i)
        #print("increase",i)
    #for i in range(65635,0,-500):
    #    utime.sleep_us(300)
    #    led.duty_u16(i)
        #print("decrease")
