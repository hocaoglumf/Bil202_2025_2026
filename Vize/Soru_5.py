'''

Bir simülasyon ortamında çalışan sensörleri yöneten bir sistem tasarlamanız istenmektedir.
Her sensör: id, location (x, y koordinatı), range (algılama yarıçapı) ve status ("active" veya "inactive") bilgilerine sahiptir.
(A)	Sınıf Tanımı
(B)	Class Attribute ve Class Method (Zorunlu): Tüm sensörlerin sayısını tutan bir attribute tanımlayınız (bir sensör nesnesi oluşturulduğunda bu sayı artmalı)
(C)	İki sensör arasındaki mesafeyi hesaplayan metodu yazınız. Bu metot class, static veya nesneye mi ait olmalıdır, karar veriniz.
(D)	Bir sensör eğer başka hiçbir sensörü algılayamıyorsa → otomatik "inactive" olur. Bunu sağlayan bir metod yazınız.


'''

import math


class Sensor:
    # (B) Class Attribute: Tüm sensörlerin toplam sayısını tutar
    total_sensor_count = 0

    def __init__(self, sensor_id, x, y, detection_range):
        self.id = sensor_id
        self.location = (x, y)
        self.range = detection_range
        self.status = "active"

        # Nesne oluşturulduğunda toplam sayıyı artırır [cite: 122, 128]
        Sensor.total_sensor_count += 1

    @classmethod
    def get_total_count(cls):
        # (B) Class Method: Sınıf seviyesinde toplam sayıya erişim sağlar
        return cls.total_sensor_count

    @staticmethod
    def calculate_distance(s1, s2):
        # (C) Karar: Statik Metot. İki farklı nesne arasındaki mesafe
        # geometrik bir işlemdir ve belirli bir nesnenin iç durumuna (self)
        # bağımlı olmak zorunda değildir. [cite: 117]
        x1, y1 = s1.location
        x2, y2 = s2.location
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def update_status_based_on_neighbors(self, all_sensors):
        """
        (D) Eğer sensör menzili içinde başka hiçbir sensör bulamazsa
        otomatik olarak 'inactive' olur.
        """
        found_neighbor = False

        for other in all_sensors:
            # Kendisi dışındaki sensörleri kontrol eder
            if other.id != self.id:
                distance = Sensor.calculate_distance(self, other)

                # Diğer sensör algılama yarıçapı (range) içindeyse
                if distance <= self.range:
                    found_neighbor = True
                    break

        # Algılama yapılamazsa durum güncellenir [cite: 45, 241]
        if not found_neighbor:
            self.status = "inactive"
            print(f"Sensor {self.id}: No neighbors detected. Status changed to INACTIVE.")
        else:
            self.status = "active"


s1 = Sensor("S1", 0, 0, 10)
s2 = Sensor("S2", 5, 5, 10)
s3 = Sensor("S3", 100, 100, 10) # Diğerlerinden çok uzak

sensor_list = [s1, s2, s3]

# Durumları güncelle
for s in sensor_list:
    s.update_status_based_on_neighbors(sensor_list)

print(f"Toplam Sensör: {Sensor.get_total_count()}") # Çıktı: 3
print(f"S3 Durum: {s3.status}") # Çıktı: inactive

