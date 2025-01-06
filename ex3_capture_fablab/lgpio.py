# Mock lgpio

def gpiochip_open(chip):
    return chip

def gpio_claim_output(gpio, pin):
    print(f"Claimed GPIO pin {pin} as output.")

def gpio_write(gpio, pin, value):
    print(f"GPIO pin {pin} set to {value}.")

def gpio_read(gpio, pin):
    return 1  # Simule une valeur par défaut

