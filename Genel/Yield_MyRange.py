def my_range(start, stop=None, step=1):
    # Eğer tek argüman verilirse (range(5) gibi)
    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError("step cannot be zero")

    current = start

    # Pozitif step
    if step > 0:
        while current < stop:
            yield current
            current += step
    # Negatif step
    else:
        while current > stop:
            yield current
            current += step



# Örnek kullanım


# Range ne döner

print(list(range(1,5)))
# bir range nesnesi (iterable) döner ve değerleri 1, 2, 3, 4 şeklindedir. Bunu bir liste olarak alabiliriz.


for i in my_range(5):
    print(i)
# 0 1 2 3 4

for i in my_range(2, 10, 2):
    print(i)
# 2 4 6 8

for i in my_range(10, 2, -2):
    print(i)
# 10 8 6 4