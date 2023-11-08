binary =[]
deciNumber = input("Decimal to binary\n")
if (deciNumber == "0"):
    print("0")
while (int(deciNumber) > 0):
    binNumber = int(deciNumber) % 2
    deciNumber = int(deciNumber) // 2
    binary.append(binNumber)
binary.reverse()
i = 0
n = len(binary)
while (i < n):
    print(binary[i], end="")
    i = i+1