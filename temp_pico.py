import machine
import utime
sensor_temp = machine.ADC(4) 
conversion_factor = 3.3 / (65535)
conversion_factor
while True:
    leitura = sensor_temp.read_u16()*convesion_factor
    temperatura = 27 - (leitura - 0.706)/0.001721
print(temperatura)
utime(2)
