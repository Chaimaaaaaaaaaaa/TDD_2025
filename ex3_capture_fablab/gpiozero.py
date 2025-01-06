# Mock gpiozero 

class Button:
    def __init__(self, pin, bounce_time=None):
        self.pin = pin
        self.is_pressed = False
        self.when_pressed = None

    def press(self):
        self.is_pressed = True
        if self.when_pressed:
            self.when_pressed()

    def release(self):
        self.is_pressed = False

