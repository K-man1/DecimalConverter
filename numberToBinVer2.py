number = int(input("Decimal to binary\n")) 
def decToBin(decimal: int):
    output = ""
    if (decimal == 0):
        return 0
    while (decimal > 0):
        binNumber = decimal % 2
        decimal = decimal // 2
        output += str(binNumber)
    output = output[::-1]
    return output
print(decToBin(number))