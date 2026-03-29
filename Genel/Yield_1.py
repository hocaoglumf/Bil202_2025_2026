'''

Fonksiyonun davranışı klasik return’den farklıdır:

1. İlk çağrı
    yield i çalışır → 0 döner
    Fonksiyon durur ama kapanmaz

2. Sonraki çağrı
    kaldığı yerden devam eder (i += 1)
    tekrar yield çalışır → 1

    Bu böyle devam eder...

'''


def sayac(n):
    i = 0
    while i < n:
        yield i
        i += 1


for x in sayac(5):
    print(x)