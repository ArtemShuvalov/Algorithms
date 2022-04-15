# Problem 4

def string_to_fraction(s: str):
    numerator = int(s[:s.find('/')])
    denominator = int(s[s.find('/')+1:])
    integer_part = str(numerator // denominator)
    remainder = numerator % denominator
    res = ""
    storage = {}
    while (remainder not in storage) and (remainder != 0):
        # Save the result to dictionary
        storage[remainder] = len(res)
        # Multiply by 10 and get the remainder of remainder
        remainder *= 10
        residual = remainder // denominator
        # Save to the value of residual
        res += str(residual)
        remainder = remainder % denominator
    if remainder == 0:
        return integer_part + '.' + res
    else:
        return integer_part + '.(' + res + ')'

print(string_to_fraction('1/3'))
print(string_to_fraction('1/2'))
print(string_to_fraction('1/8'))
