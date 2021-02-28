import machine
pin = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(25, machine.Pin.OUT)
#pin = machine.PIN(/)

while True:
    if pin.value():
        led(1)
        print("INTRUSO DETECTADO!!!!!!!!!!!!!")
    led(0)
    print("NAO TEM NINGUEM!!!!!!!!!!!!!")
    

