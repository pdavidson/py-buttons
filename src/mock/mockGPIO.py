

class GPIO:

    FALLING = "FALLING"
    RISING = "RISING"
    IN = "IN"
    OUT = "OUT"
    BCM = "BCM"
    HIGH = "on"
    LOW = "off"

    def __init__(self):
        print ("Constructing mock GPIO")

    @staticmethod
    def setmode(mode):
        print ("Setting mode " + mode)

    @staticmethod
    def setup(pins, in_out):
        print ("Setting pin " + ', '.join(str(x) for x in pins) + ' to ' + in_out)

    @staticmethod
    def add_event_detect(pin, mode, callback, bouncetime):
        print ("Adding event detection for pin " + str(pin) + ' alert on ' + mode + " bounce "
               + str(bouncetime) + " callback function " + str(callback))

    @staticmethod
    def output(light, on_off):
        print ("turning light " + str(light) + " " + on_off)