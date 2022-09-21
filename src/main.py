# main.py
from machine import Pin
from time import sleep

pin2 = Pin(2, Pin.OUT);
pin2.on();

sleep(0.5);
pin2.off();