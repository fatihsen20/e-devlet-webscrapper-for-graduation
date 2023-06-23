# E-devlet Üzerinden Mezuniyet Durumu Sorgulama
- ### E-devlet üzerinden mezuniyet durumu sorgulama işlemi için gerekli olan bilgileri kullanarak sorgulama işlemi yapar.
- ### Sorgulama işlemi sonucunda mezun olmuşsanız size bir bilgilendirme mail'i gönderir.
- ### Bot, python ve selenium ile yazılmıştır.

## Kurulum
- ### Öncelikle .env dosyasını oluşturmanız gerekmektedir. .env dosyası içerisine aşağıdaki bilgileri yazmanız gerekmektedir.
```bash
tc= # TC Kimlik Numaranız
e_password= # E-devlet şifreniz
from_mail= # Mail adresiniz
mail_password= # Mail şifreniz
to_mail= # Mail göndermek istediğiniz adres
```

### 1. Yöntem: Python kurulumu
- Bu yöntem ile kendi bilgisayarınızda çalıştırabilirsiniz. Sürüm sorunlara ortaya çıkabileceği için bu yöntemi önermiyorum.
- Gereksinimler:
    - Python 3.6 veya üstü
    - pip
    - Google Chrome
    - .env Dosyası
```python
pip install -r requirements.txt
python3 bot.py
```

### 2. Yöntem: Docker kurulumu
- Bu yöntem ortam farklılıklarını ortadan kaldırdığı için önerilen yöntemdir.
- Gereksinimler:
    - Docker
    - .env Dosyası
```bash
docker build -t mezuniyetbotu .
docker run -it mezuniyetbotu
```

## Kullanım
- Bot'u istediğiniz zaman yukarıdaki adımlara göre çalıştırabilirsiniz.
- Otomatik olarak her gün 1 saatte bir çalıştırılması için crontab kullanabilirsiniz.
- Crontab kullanımı için aşağıdaki adımları takip edebilirsiniz.
```bash
crontab -e
```
- Açılan editörde aşağıdaki satırları ekleyin.
```bash
0 * * * * docker run -d mezuniyetbotu
```
- Bu satır ile her saat başı bot çalıştırılacaktır.
- Daha fazla bilgi için [crontab](https://crontab.guru) kullanımına bakabilirsiniz.
