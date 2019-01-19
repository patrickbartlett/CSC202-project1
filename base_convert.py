


def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""

    mod = num % b

    # base case
    if num < 2:
        return str(num)
    # recursive call + add on remainder, converted to hex; whole thing trimmed of leading 0s
    else:
        return trim(str(convert(num//b, b)) + str(convert_hex(mod)))



def trim(string):
    """trims leading 0s"""
    while string[0] == '0':
        string = string[1:]
    return string

def convert_hex(num):
    """converts numbers to letter, for higher bases"""
    if num < 10:
        return num
    elif num == 10:
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'
    else:
        raise RuntimeError


