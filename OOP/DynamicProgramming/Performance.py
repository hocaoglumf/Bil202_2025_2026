import time

def fonksiyon():
    toplam = 0
    for i in range(10_000_000):
        toplam += i
    return toplam

baslangic = time.perf_counter()

fonksiyon()

bitis = time.perf_counter()

print(f"Geçen süre: {bitis - baslangic:.6f} saniye")