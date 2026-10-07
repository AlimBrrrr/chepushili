def func1(a):
    sign = '1' if a < 0 else '0'
    
    return sign + bin(abs(a))[2:]

def direct_to_additional(direct): 
    if direct[0] == "0": return direct
    inverted = ""

    for bit in direct:
        if bit == "0":
            inverted += "1"
        else:
            inverted += "0"

    additional = bin(int(inverted, 2) + 1)[2:]
    return additional.zfill(len(direct))
print(direct_to_additional("10001101"))