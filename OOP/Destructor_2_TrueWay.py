
'''
Tavsiye edilen  kullanım.
'''
class FileHandler:
    def __init__(self):
        self.file = None

    def CreateFile(self, filename):
        self.file=open(filename, "w")
        print("File opened")

    def write(self, text):
        self.file.write(text)

    def CloseFile(self):
        self.file.close()
        print("Closing file")


    def __del__(self):
        print("Goodbye")


f = FileHandler()
f.CreateFile("test.txt")
f.write("Hello")
f.CloseFile()
del f