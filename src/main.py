# main.py
from time import sleep
from machine import Pin

# IR library from: https://github.com/peterhinch/micropython_ir
from ir_rx.sony import SONY_20 as SonyRx
from ir_tx.sony import SONY_20 as SonyTx

pin2 = Pin(2, Pin.OUT)
for x in range(3):
    pin2.on()
    sleep(0.2)
    pin2.off()
    sleep(0.2)


def callback(data, addr, ctrl):
    if data < 0:  # NEC protocol sends repeat codes.
        print('Repeat code.')
    else:
        print('Data {:02x} Addr {:04x} Ctrl {:04x}'.format(data, addr, ctrl))


sender = SonyTx(Pin(21))
receiver = SonyRx(Pin(23, Pin.IN), callback)
i = 0

while True:
    pin2.off()
    sleep(0.9)
    pin2.on()
    # Sony 20 supports up to: Max addr: 0x1f, data: 0x7f, toggle: 0xff
    sender.transmit(0x1f, i, 0xff)
    i += 1
    i = i % 0x7f
    sleep(0.1)
