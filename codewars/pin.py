def validate_pin1(pin):
    return True if (len(pin) == 4 or len(pin) == 6) and pin.isdigit() else False

def validate_pin2(pin):
    return len(pin) in (4, 6) and pin.isdigit()

print(validate_pin1("1"))
print(validate_pin1("12"))
print(validate_pin1("123"))
print(validate_pin1("1234"))
print(validate_pin1("12345"))
print(validate_pin1("123456"))

print(validate_pin1("a234"))
print(validate_pin1(".234"))
print(validate_pin1("-123"))