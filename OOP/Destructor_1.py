'''

Garbage collector kullanımı

Bu örnek, Python’da bir nesnenin fonksiyon içindeki yaşam döngüsünü (lifecycle) ve __del__ metodunun
ne zaman çalışabileceğini göstermek için oldukça güzel bir örnektir.


Destructor Ne Zaman Çalışır?

Eğer:

✔ Başka referans yoksa
✔ Garbage collector devreye girerse, -ki func() scope çıkışı collector'ü çağırır.
 __del__ çalışır

'''
class Test:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")

def func():
    t = Test()

func()
func()