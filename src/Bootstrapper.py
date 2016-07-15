from mock.mockGPIO import GPIO
from Lights import red, green, yellow, light_pins


class Bootstrapper:

    buttonA = 1  # Pin 1
    buttonB = 2  # Pin 2
    buttonC = 3  # Pin 3

    buttonReset = 4 # Pin 4

    codes = {buttonA: "a", buttonB: "b", buttonC: "c"}

    def __init__(self, stoplight):
        self.stoplight = stoplight

    def bootstrap(self):
        Bootstrapper.__bootstrap_gpio()
        Bootstrapper.__bootstrap_inputs()
        Bootstrapper.__bootstrap_outputs()
        self.__bootstrap_callbacks()

        yellow()

    @staticmethod
    def __bootstrap_gpio():
        print ("bootstrapping GPIO")
        GPIO.setmode(GPIO.BCM)

    @staticmethod
    def __bootstrap_inputs():
        print ("bootstrapping inputs")
        GPIO.setup([Bootstrapper.buttonA, Bootstrapper.buttonB, Bootstrapper.buttonC], GPIO.IN)

    @staticmethod
    def __bootstrap_outputs():
        print ("bootstrapping outputs")
        GPIO.setup(light_pins, GPIO.OUT)

    def __bootstrap_callbacks(self):
        print ("bootstrapping callbacks")
        GPIO.add_event_detect(Bootstrapper.buttonA, GPIO.FALLING, callback=self.click_callback, bouncetime=200)
        GPIO.add_event_detect(Bootstrapper.buttonB, GPIO.FALLING, callback=self.click_callback, bouncetime=200)
        GPIO.add_event_detect(Bootstrapper.buttonC, GPIO.FALLING, callback=self.click_callback, bouncetime=200)

    def click_callback(self, channel):
        print("Channel " + channel + " clicked")
        if channel == Bootstrapper.buttonReset:
            self.__reset()
        else:
            value = Bootstrapper.codes[channel]

            print("Pushing value " + value)
            self.stoplight.push(value)

        valid = self.stoplight.validate()

        if valid:
            green()
        else:
            red()

    def __reset(self):
        yellow()
        self.stoplight.reset()




