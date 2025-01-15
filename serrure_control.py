import RPi.GPIO as GPIO
import time

# Configuration des broches GPIO
PIN_SERRURE = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_SERRURE, GPIO.OUT)

def verrouiller():
    GPIO.output(PIN_SERRURE, GPIO.HIGH)
    print("Serrure verrouillée.")

def deverrouiller():
    GPIO.output(PIN_SERRURE, GPIO.LOW)
    print("Serrure déverrouillée.")
