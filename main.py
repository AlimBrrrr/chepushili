direct = input("Введите прямой код: ")
if direct[0] == "0": 
    additional = direct 
else: 
    inverted = ""
for bit in direct:
    if bit == "0":
        inverted += "1"
    else:
        inverted += "0"

additional = bin(int(inverted, 2) + 1)[2:]
additional = additional.zfill(len(direct))
print("Дополнительный код:", additional)