
'''
Tavsiye edilmeyen kullanım.

Doğru yöntem dosyayı kapatım sonra nesneyi silmektir.
Nesneyi silerken dosyayı kapatmak tuatarsızlığa sebebiyet verebilir.

'''
class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, "w") # burada dosya açmak iyi bir fikir değil
        print("File opened")

    def write(self, text):
        self.file.write(text)

    def __del__(self):
        print("Closing file")
        self.file.close()


f = FileHandler("test.txt")
f.write("Hello")
del f