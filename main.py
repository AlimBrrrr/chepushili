def func1(a):
    sign = '1' if a < 0 else '0'
    
    return sign + bin(abs(a))[2:]
