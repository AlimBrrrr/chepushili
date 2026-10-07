def func1(a):
    sign = '1' if a < 0 else '0'
    
    return sign + bin(abs(a))[2:]

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
