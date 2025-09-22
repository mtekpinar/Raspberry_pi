from gpiozero import LED
from time import sleep

#16.09.2025 saat 15:42 led on off yapıldı.

led = LED(18) # Buradaki bmc numarası = gpio numarasıdır


while True:
    
    led.on()
    sleep(1)
    led.off()
    sleep(1)
