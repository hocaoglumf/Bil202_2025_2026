'''

1. Model (Veri Katmanı)

Uygulamanın veri yapısını ve iş mantığını (business logic) temsil eder. Veritabanı işlemleri, verinin doğrulanması ve hesaplamalar burada yapılır.
2. View (Arayüz Katmanı)

Kullanıcının gördüğü kısımdır (HTML, CSS, JSON vb.). Modelden gelen veriyi kullanıcıya sunar.
3. Controller (Kontrol Katmanı)

Kullanıcıdan gelen istekleri (request) karşılar, Model ve View arasındaki köprüyü kurar. İsteğe göre Model'den veri çeker ve hangi View'un gösterileceğine karar verir.

'''


import JobView as JV
import JobModel as JM
import JobController as JC



# Başlatma
model = JM.JobModel()
view = JV.JobView()
controller = JC.JobController(model, view)

# Kullanıcı Etkileşimi
controller.list_jobs()
controller.create_job("Cylinder Polishing", "15h")
controller.list_jobs()