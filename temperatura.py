import machine
import utime
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
while True:
    leitura = sensor_temp.read_u16() * conversion_factor
    temperatura = 27 - (leitura-0.706)/0.001721
print(temperatura)
utime(2)