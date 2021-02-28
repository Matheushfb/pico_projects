import machine

pin = machine.ADC(machine.Pin(28))

while True:
    pin.read(read_u16())




