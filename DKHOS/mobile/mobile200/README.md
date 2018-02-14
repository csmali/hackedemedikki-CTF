# Mobile 200

## Tutmayın küçük enişteyi

Öncelikle apk'nın source kodlarını jadx-gui toolunu kullanarak inceledim. İlk olarak AndroidManifest.xml'de tanımlı izinlere göz attım. MainActivity'yi tespit etmek dışında buradan bir şey çıkmadı.
MainActivity'i incelemeye devam ettim. onCreate() apk'nın emulatorde çalışmasını engelleyen bir kontrol olduğunu fark ettim.

![ilk](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/mobile/mobile200/1.png "ilk")

Ardından apktool ile apk'yı twoOut adlı klasöre decompile ettim.

![iki](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/mobile/mobile200/2.png "iki")

Android Studio ile yeni bir android projesi oluşturdum. twoOut içinden çıkan Resources ve Manifesti yeni projeye aktardım. Bu işlem yapılırken tabii ki bazı path isimlerinin yeni android projesine göre düzenlenmesi gerekiyor fakat onları buraya detaylı olarak yazmayacağım, Android studio gerekli uyarıları veriyor.

![uc](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/mobile/mobile200/3.png "uc")

![dort](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/mobile/mobile200/4.png "dort")

Daha sonra MainActivity.java, a.java ve b.java'yı da yeni projeye aktardım. Bu aşamada gerekli importların yapılması,pathlerin düzeltilmesi ve exception handling işlemlerini yaparak kodu build edebilir hale getirdim. Kodu çalıştırmayı denedim fakat koddaki getDataDir() metodu exception fırlatıyordu.

![bes](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/mobile/mobile200/5.png "bes")

Bu hatayı çözmenin yolu api 24 ve ya daha sonrasını kullanan bir emulator kullanmak. Kullandığım emulatoru değiştirerek tekrar çalıştırdım, bu sefer uygulama açılıyor fakat onCreate()'te tespit ettiğimiz kontrole takılıyordu.

![alti](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/mobile/mobile200/6.png "alti")

Bunu aşmak için aşağıdaki kod parçasını onCreate() metodundan sildim.
 
 if (a(getApplicationContext()).booleanValue()) {
            Toast.makeText(this, "Emulator detected.", 1).show();
            return;
 }

Uygulamayı tekrar çalıştırdığımda Emulator detectionu aşmış oldum ve uygulama aşağıdaki log'u basıyordu:

	>> 8WTSZJn26p9xdrTuxcedV/GOftOrQKtfRcNw9YOTSts=

onCreate() metodunu inceleme başladım. k() metodunun çağrıldığını gördüm. Bu metodda a("suport", a.a(b.cZ)); şeklinde bir metod kullanılmış. b.cZ'de bir string tutuluyor.
b sınıfını incelediğimde bu stringin "n**NTS**o**NTS**t**NTS**-**NTS**c**NTS**a**NTS**c**NTS**h**NTS**e**NTS**".replace("**NTS**",""); ile bulunduğunu yani kısaca değerinin 'not-cache' oldugunu gördüm.
a sınıfındaki string a(String str) metodu ise input alarak aldığı stringin md5 hashini dönüyordu. Yani a.a(b.cZ) ifadesi "not-cache" in md5 hashi olan 0f5347b7a11435c3b3396d2db4db76c4 değerini dönüyor.
Artık elimizde a("suport","0f5347b7a11435c3b3396d2db4db76c4") ifadesi var. Bu metodu incelediğimde raw package'ının altındai "suport" isimli dosyanın decrypt edilerek "decr" isimli yeni bir dosyaya yazıldığını gördüm. Burada AES cipher ve anahtar olarak daha önce hesapladığımız hash değeri olan "0f5347b7a11435c3b3396d2db4db76c4" kullanılmış. Daha sonra bu "decr" dosyası "tolof" isimli farklı bir dosyaya kopyalandıktan sonra siliniyor. "tolof" dosyası ise data/data'nın altında uygulamaya ayrılmış olan alanda "cachezxclc" adlı bir klasörde bulunuyor ve buradan dex classları load edildikten sonra dosya siliniyor. Dosyanın silinmemesi için ilgili komutu command out ediyoruz.


![yedi](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/mobile/mobile200/7.png "yedi")

Daha sonra tolof.dex dosyasını emulatorden aşağıdaki komut ile çekiyoruz:

adb pull /data/data/com.mfc.mobile200/cachezxclc/tolof.dex .

Artık elimizde bir dex dosyası var. Bu dex dosyasını okunabilir bir source koduna çevirmemiz gerek. Bu nedenle jadx-gui'nin de açabileceği jar formatına çeviriyoruz. Bunun için sırasıyla aşağıdaki komutları kullanıyoruz.

adb pull /system/framework
java -jar baksmali.jar deodex tolof.dex -b framework/x86/boot.oat -o out
java -jar smali.jar ass ./out -o app.dex
d2j-dex2jar.sh app.dex -o newapk.jar

![sekiz](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/mobile/mobile200/8.png "sekiz")

Not: Bu işlemleri yapabilmek için https://bitbucket.org/JesusFreke/smali/downloads/ adresinden baksmali.jar ve smali.jar'larını indirebilirsiniz.

Bu aşamada jadx-gui ile yeni oluşan newapk.jar'ı açıyoruz. Ve t class'ındaki b metodu dikkatimizi çekiyor. Bu metod input olarak aldığı Stringi yine input olarak aldığı key ile AES kullanarak decrpyt ediyor. 

![dokuz](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/mobile/mobile200/9.png "dokuz")

Bu b metodunu kendi oluşturduğumuz projeye alıyoruz ve onCreate() metodunda aşağıdaki şekilde çağırıyoruz ve log olarak bastırıyoruz.
Buradaki ilk parametremiz yeni ciphered textimiz, uygulamanın ilk çalıştığı anda log olarak bastığı string olacak. ("8WTSZJn26p9xdrTuxcedV/GOftOrQKtfRcNw9YOTSts=")
İkinci parametremiz yani keyimiz ise daha önce hesapladığımız md5 hash değeri olacak. ("0f5347b7a11435c3b3396d2db4db76c4")

![on](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/mobile/mobile200/10.png "on")

Ve flagi logdan elde ediyoruz: D/FLAG: DKHOS_{salin_beni_gideyim}

![onbir](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/mobile/mobile200/11.png "onbir")



