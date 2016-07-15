__buttonA = 1  # Pin 1
__buttonB = 2  # Pin 2
__buttonC = 3  # Pin 3

__buttonReset = 4 # Pin 4


buttons = [__buttonA, __buttonB, __buttonC, __buttonReset]

__codes = {__buttonA: "a", __buttonB: "b", __buttonC: "c"}

def is_reset(channel):
    return channel == __buttonReset

def get_code(channel):
    return __codes[channel]