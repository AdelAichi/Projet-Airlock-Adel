import machine
import time

def activer_mode_basse_conso():
    print("Activation du mode basse consommation.")
    rtc = machine.RTC()
    rtc.irq(trigger=machine.Pin.WAKE_HIGH, wake=machine.DEEPSLEEP)
    machine.deepsleep()
