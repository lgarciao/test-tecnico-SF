def validate_pin(pin):
    if len(pin) not in [4, 6]:
        return False
    return pin.isdigit()