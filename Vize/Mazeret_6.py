class Banka:
    def __init__(self, bakiye):
        self.__bakiye = bakiye

    def bakiye_goster(self):
        return self.__bakiye

hesap = Banka(1000)
hesap.__bakiye = 500  # Yeni bir değişken mi yaratır yoksa var olanı mı değiştirir?

print(hesap.bakiye_goster())
