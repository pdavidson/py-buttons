from mock.mockGPIO import GPIO
from Lights import red, green, yellow, lights
from Buttons import buttons, is_reset, get_code


class Bootstrapper:

    def __init__(self, stoplight):
        self.stoplight = stoplight

    def bootstrap(self):
        print ("bootstrapping GPIO")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(buttons, GPIO.IN)
        GPIO.setup(lights, GPIO.OUT)
        self.__bootstrap_callbacks()

        yellow()

    def __bootstrap_callbacks(self):
        print ("bootstrapping callbacks")
        GPIO.add_event_detect(buttons, GPIO.FALLING, callback=self.click_callback, bouncetime=200)

    def click_callback(self, channel):
        print("Channel " + channel + " clicked")

        if is_reset(channel):
            print ("Resetting")
            yellow()
            self.stoplight.reset()
        else:
            value = get_code(channel)
            print("Pushing value " + value)
            self.stoplight.push(value)
            valid = self.stoplight.validate()

            if valid:
                green()
            else:
                red()