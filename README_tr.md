
# CryptoFactory.exe - Sahte BTC Mining Uygulaması

## Kullanılan Dil(ler)

<picture>
  <source srcset="https://skillicons.dev/icons?i=py" media="(prefers-color-scheme: dark)">
  <img src="https://skillicons.dev/icons?i=py">
</picture>


```markdown

**CryptoFactory.exe**'ye hoş geldiniz. Forklayıp, yıldız bırakıp takip ederseniz çok sevinirim, içeriğe geçelim; – Python ve PyQt5 ile geliştirilmiş gerçekçi bir program. Sahte GPU istatistikleri ve performans verilerini gerçek zamanlı olarak grafikleştirme yeteneği ile kripto para madenciliği sürecini taklit eder.

## Özellikler

- **Gerçek Zamanlı Madencilik Simülasyonu**: Uygulama, hız, ortalama süre ve GPU performansı gibi sahte istatistikler göstererek madencilik işlemlerini simüle eder.
- **BTC Fiyat Alma**: Uygulama, CoinGecko API'sinden gerçek zamanlı Bitcoin fiyatını alır.
- **Performans Verileri**: Kullanıcılar, madencilik performans verilerini görebilir ve Matplotlib kullanarak hız ve ortalama süreyi grafikleştirebilir.
- **GPU Bilgileri**: Sıcaklık, yük ve bellek kullanımı gibi sahte GPU istatistikleri gösterilir.
- **BTC ve USD Değerleri**: Uygulama, madencilik ilerledikçe sahte Bitcoin ve USD değerlerini takip eder ve gösterir.
- **Kullanıcı Etkileşimi**: İstediğiniz zaman madenciliği başlatın ve durdurun. Ayarlar, hakkında ve destek bağlantıları gibi ek özellikleri keşfedin.

## Bağımlılıklar

Uygulamayı çalıştırmak için aşağıdaki Python kütüphanelerinin yüklü olması gerekir:

- `PyQt5`: GUI oluşturmak için (Adamsın)
- `requests`: Gerçek zamanlı BTC fiyatlarını almak için 
- `matplotlib`: Performans verilerini grafikleştirmek için

### Linux'ta Bağımlılıkların Yüklenmesi

Linux kullanıcıları, gerekli bağımlılıkları şu şekilde yükleyebilir:

1. **Python 3'ü Yükleyin**: Python 3'ün yüklü olduğundan emin olun.
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```

2. **PyQt5'i Yükleyin**:
    ```bash
    sudo apt install python3-pyqt5
    ```

3. **Ek Python Kütüphanelerini Yükleyin**:
    ```bash
    pip3 install requests matplotlib
    ```

Eğer `PyQt5` paket yöneticinizde mevcut değilse, pip ile şu şekilde kurabilirsiniz:

```bash
pip3 install PyQt5
```

## Nasıl Çalıştırılır

### Linux'ta Çalıştırma

1. **Depoyu Klonlayın**:
    ```bash
    git clone <https://github.com/l1ve709XXD/CryptoFactory-1.6.git>
    cd <main.py>
    ```

2. **Betiği çalıştırılabilir hale getirin**:
    ```bash
    chmod +x main.py
    ```

3. **Uygulamayı çalıştırın**:
    ```bash
    ./main.py
    ```

Alternatif olarak, doğrudan Python 3 ile çalıştırabilirsiniz:
```bash
python3 main.py
```

## Dosya Genel Bakışı

- **main.py**: Sahte madencilik uygulamasını çalıştıran ana Python dosyası.
- **background.jpg**: Ana pencerede kullanılan isteğe bağlı bir arka plan görüntüsü dosyası. `main.py` ile aynı dizinde olduğundan emin olun.

## İşlevsellik

### Madenciliği Başlat/Durdur
- **Madenciliği Başlat**: Kripto para madenciliğini simüle etmek için `RUN` düğmesine tıklayın.
- **Madenciliği Durdur**: Simülasyonu durdurmak için `STOP` düğmesine tıklayın.

### Cüzdan ve İşlemler
- Madencilik işlemi sırasında sahte Bitcoin ve USD cüzdan değerlerinizi izleyin.

### GPU İstatistikleri
- Gerçek zamanlı olarak güncellenen sahte GPU bilgilerini (örneğin sıcaklık, bellek kullanımı) gösterir.

### Performans Verileri
- Uygulama performans verilerini kaydeder ve **Performans Verilerini Grafikleştir** düğmesi ile görselleştirebilirsiniz.

## Ayarlar ve Özelleştirme

- **Tema**: Ayarlar penceresinden açık ve koyu temalar arasında geçiş yapın.
- **Hakkında ve Destek**: Ek bilgi ve destek için harici bir web sitesine ve Discord sunucusuna bağlantılar.

## Linux'a Özel Notlar

- **İzin Sorunları**: Betiği çalıştırırken izin sorunlarıyla karşılaşırsanız, `main.py` dosyasının çalıştırılabilir olduğundan emin olun (`chmod +x main.py`).
- **Python Sürümü**: Python 3 kullandığınızdan emin olun. Bazı dağıtımlar hala varsayılan olarak Python 2 kullanıyor olabilir.
- **PyQt5 Kurulumu**: `apt` ile PyQt5 kurulumu sırasında sorun yaşıyorsanız, pip kullanarak kurmayı deneyin (`pip3 install PyQt5`).

## Gelecek Geliştirmeler
- Gerçek zamanlı madencilik havuzu etkileşimi ekleyin.
- Gerçek zamanlı donanım izleme ile GPU bilgilerini iyileştirin.

## Lisans

Bu proje GPL-3.0 lisansı altında lisanslanmıştır.

```

### Linux İçin Özel Eklemeler:
- **Bağımlılık Kurulumu**: Linux'ta Python, PyQt5 ve diğer bağımlılıkların nasıl kurulacağını açıklayan ayrıntılı adımlar.
- **Uygulamanın Çalıştırılması**: Python betiğini çalıştırılabilir hale getirme ve terminal üzerinden çalıştırma adımları.
- **Linuxa Özel Notlar**: İzin sorunları, Python 3 kullanımı ve PyQt5 kurulumuyla ilgili ipuçları.
```


## Discord Hesabım

![My Discord](https://lantern.rest/api/v1/users/794909914760871967?svg=1&theme=dark&borderRadius=2&hideActivity=1&hideStatus=0)
