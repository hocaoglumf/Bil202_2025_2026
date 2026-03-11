'''

decimal_to_base fonksiyonu onluk tabandaki (decimal) bir sayıyı verilen başka bir tabana dönüştürür.
Desteklenen taban aralığı 2 ile 36 arasındadır.
'''


def decimal_to_base(n, base):
    if base < 2 or base > 36:
        raise ValueError("Taban 2 ile 36 arasında olmalıdır.")

    if n == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    negative = False
    if n < 0:
        negative = True
        n = abs(n)

    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n //= base

    if negative:
        result = "-" + result

    return result

print(decimal_to_base(225,27))