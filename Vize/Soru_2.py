class Music:
    @staticmethod
    def play():
        print("*playing music*")

    def stop(self):
        print("stop playing")

    @classmethod
    def Pause(cls):
        print("Music paused ")

Music.play()
m=Music()
m.stop()

Music.Pause()