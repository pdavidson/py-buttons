from mock.mockGPIO import GPIO

__green = 15  # Pin LED Green
__yellow = 16  # Pin LED Yellow
__red = 17  # Pin LED Red

lights = [__green, __yellow, __red]

def red():
    __off(__green)
    __on(__red)
    __off(__yellow)


def green():
    __on(__green)
    __off(__red)
    __off(__yellow)


def yellow():
    __off(__green)
    __off(__red)
    __on(__yellow)


def __on(light):
    GPIO.output(light, GPIO.HIGH)


def __off(light):
    GPIO.output(light, GPIO.LOW)
