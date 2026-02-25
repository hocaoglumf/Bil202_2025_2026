

def decimal_to_base(n, base):
    alfabe="0123456789ABCDEFGHIJKLMNOPRSTUXVYZ"
    number=""



    if n==0:
        return "0"

    pozitif=n>0

    if not(pozitif):
        n = abs(n)

    while n>0:
        kalan=n%base
        if kalan > len(alfabe):
            return "Error"
        number = alfabe[kalan]+number
        n //=base

    if not(pozitif):
        number = "-"+number
    return number


print(decimal_to_base(23,5))
print(decimal_to_base(47,12))
print(decimal_to_base(65,18))
print(decimal_to_base(123,33))
print(decimal_to_base(-123,33))
print(decimal_to_base(123,145))

