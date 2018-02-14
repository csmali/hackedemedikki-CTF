# Forensics400 

## Hafıza Kaybı

Selamlar arkadaslar DKHOS CTF’inde hackedemedikki(ki ayri) takimi olarak yaristik.  Bu yazida for400 sorusunun cozum yontemini anlatacagim.

Bize bir adet memory image verilmis durumda. Onceki CTF’lerden kullandigim ve okudugum kadariyla volatility kullanilacagini anliyoruz. Imagei okuyabilmek icin bir isletim sistemi profili secmemiz gerekiyor. Bu profili tespit etmek icin su komutu kullaniyoruz.

    volatility -f for400.img imageinfo

![ilk](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/forensics/forensics400/1.jpg "ilk")

Ardindan volatility pluginlerini kullanmak icin profili set etmemiz gerekiyor ve buldugumuz profili yazip “psscan” plugini ile o makinedeki processleri inceliyoruz.


![iki](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/forensics/forensics400/2.jpg "iki")

Processleri incelerken gozumuze kucuk form.exe takiliyor . form.exe 2420 process idsi 0x000000003fd57548 offsetiyle ve hic de tanidik olmadigimiz ismiyle tek goz odada yasiyor.

Processlerin dumplarini alacagiz bu kisimda. Sadece form.exeyi de alabiliriz ancak emin olmak adina butun processlerin dumpini, yarattigimiz memdump klasorune aliyoruz.

![uc](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/forensics/forensics400/3.jpg
 "uc")

Butun processlere ait datayi inceleyebilecegimiz bir noktaya geldik. Simdi 2420.dmp  dosyasini yakindan inceleyelim.

![dort](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/forensics/forensics400/4.jpg "dort")

Processin icerisinde bir yerlerde flag.txt dosyasinin tutuldugunu gorduk ve binwalkla baktigimizda rar archive oldugunu tespit ettik ve extract ettik. Hemen icerisindeki dosyayi inceleyelim. Binwalkla rar dosyasininin header kismindan tutup ayirabilmisiz. Hexdump ile inceleyelim.


![bes](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/forensics/forensics400/5.jpg "bes")
![alti](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/forensics/forensics400/6.jpg "alti")

Guzel. Bir rar dosyasinin icinde flag.txt duruyor. Icerigi cok guzel gorunmuyor.Encrypted oldugunu varsayarak ilerliyoruz. Bi yerlerden password(sifre degil parola xd) bulabilirsek fena olmaz.

CTF esnasinda yapabilmistim ancak tekrar ederken binwalkla beceremedigim icin rar dosyasini ayirabilmek icin online hex editorlerden birini kullaniyoruz Rar kismi bitene kadarki hex kodunu kopyalayip yapistirdik ve rar dosyasini yalniz birakip download ettik.


![yedi](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/forensics/forensics400/7.jpg "yedi")

Rar dosyasini bilgisayarimiza indirdikten sonra unrar ile acmaya calisiyoruz ve password istedigini goruyoruz.
![sekiz](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/forensics/forensics400/8.jpg "sekiz")

Volatility kullanimini cok iyi bilmedigim icin bu noktadan sonra saatlerim  dokumantasyon okumakla gecti. Memory dumpta neler olabilir ,hangi pluginleri kullanarak ne elde edebiliriz gibi seyleri okudum.Link de burda volatility reference ve tam umudumu kesmisken clipboard pluginini gordum

Bircok elementi tanidik bircok elementi gorduk simdi geldik en civcivli bolume. Memory dump alindigi esnada clipboardda ne varsa size gosteren komutu giriyoruz

![dokuz](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/forensics/forensics400/9.jpg "dokuz")

Text olarak datayi kopyaliyor ve rar dosyasini acmak icin kullaniyoruz.

![on](https://github.com/csmali/hackedemedikki-CTF/blob/master/DKHOS/forensics/forensics400/10.jpg "on")

DKHOS_{its_N0t_A_BuG_it_is_a_feature}

neler ogrendik peki ?

    arkadaslar RTFM plz.
    soruyu cozebilmeniz icin o sorunun cozumunu yarismadan once zaten biliyor olmaniza gerek yok. yarisma esnasinda da ogrenebilirsin.
    soruyu cozemeyince salmayin. ne var ne yok her seyi deneyin.

Yarismadaki sorular cok dikkatle hazirlanmis ve guzel sorulardi. Puanlamasi da cok dengeliydi. Prodaft ekibine tesekkur etmek gerekiyor ellerine saglik.
