userInput = int(input("Decimal to selected base.\n"))
userBase = int(input("What base would you like?\n"))
def baseConverter(base):
    if (base<10 and base>=0): 
        return chr(base + ord("0"))
    else:
        return chr(base - 10 + ord("A"))
def deciToBase(base, input, output):
    while input > 0:
        output += baseConverter(input % base)
        input = int(input / base)
    output = output[::-1]
    return output
print(deciToBase(userBase, userInput, ""))