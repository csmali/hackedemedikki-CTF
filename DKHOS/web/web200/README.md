### KIMIZIM KANDAN BAHTIM KARADAN (Web 200 + 20)
![soru][soru.png]

Soru metni sadece bir IP adresi içeriyor. Verilen IP adresine tarayıcı ile eriştiğimizde de **not found** ile karşılaşıyoruz.

![adim1][adim_1.png]

Bu aşamada aklımdan dirbuster gibi bir araçla sunucudaki klasörleri bruteforce etmek geçti. Ancak ağır silahları çıkartmadan önce tüm detayları kontrol ettiğimden emin olmak istedim. Önceki CTFlerde HTTP başlıkları veya HTML kaynak kodunu incelemediğim için boşa harcadığım zamanların tecrübesi sağolsun, sitenin kaynak kodunu CTRL + U kısayolu ile açtım. 

![adim2][adim_2.png]

Kaynak kodunda HTML yorumu içine gizlenmiş `/site` alt klasörünü görüyoruz.

![adim3][adim_3.png]

`/site` alt klasörüne gittiğimizde bir blog sayfası ile karşılaşıyoruz. Bu aşamada site içinde kaybolmak çok kolaydı. Bu soruyu çözmüş olanların bloglarını okuduğunda birçok kişi bu aşamada sitenin içine dalıp çok uzun süre açık aramışlar. Ben biraz daha şanslıydım bu noktada. Açılan sayfaya göz attığımda en alttaki `development version: dev` yazısını fark ettim. `dev` linkine tıkladığımda beni `http://dev` adresine yönlendirdi ve geçerli bir domain ismi  olmadığı  için tabiki DNS resolve etmedi. 

Burada aklıma sunucunun *Virtual Hosting* kullanabileceği geldi. En basit şekilde açıklarsak, *Virtual Hosting* bir sunucunun tek bir IP adresi üzerinden birden çok domain adresini **host** etmesini sağlar. Aşağıdaki resimde görüleceği üzere `Example1.com` ve `Example2.com`'a tek bir IP üzerinden erişilebiliyor. *Virtual Hosting* aktif edilmiş sunucular gelen isteklerin `Host` HTTP başlığına bakarak yönlendirir.

![apache2][apache2_2.jpg]

Gönderilen isteğin `Host` HTTP başlığını değiştirmek için Burp Suite Proxy'nin Repeater aracını kullandım. (Zed Attack Proxy veya Google Chrome Eklentisi olan Host Tool da kullanabilirsiniz: https://chrome.google.com/webstore/detail/host-tool/naheccckleemcckamjkhdihboannlgll?hl=en)

![adim4][adim_4.png]

`Host` başlığını dev yapıtığımda ve isteği gönderdiğimizde karşımıza yeni bir URL çıkıyor.

![adim5][adim_5.png]

URL'i ziyaret ettiğimizde bize sunucunun Python kaynak kodunu dönüyor. Kaynak kodunu incelediğimizde bazı kelimelerin filtrelendiğini görüyoruz ve ayrıca `get_flag()` fonksiyonu bize flag'in /flag dosyasında değil de bir environment değişkeni olarak saklandığını gösteriyor. Eğer istekte gönderdiğimiz `name` parametresi filtreye takılmaz ise bize `name` ismine sahip dosyanın içeriğini dönüyor. Burada Google'da arama yaptım ve environment değişkenlerinin  `/proc/self/environ` dosyasında saklandığını öğrendim. Ancak filtrede `proc` kelimesi yasaklı olduğu için  `/file?name=/proc/self/environ` isteği bir işe yaramazdı.

Bu durumda eğer `/proc/self/environ`'a  sysmlink yapan bir dosya bulabilirsek filtreye takılmadan flagi bulmuş oluruz. Bunun için tekrar Google'a döndüm.

![adim6][adim_6.png]

Dönen linklerden ilkine tıkladığımızda aynı problemin 2017 Google CTF'inde sorulmuş olduğunu görebiliriz. Oradaki abilerimiz çok güzelce(amma İngilizce) açıklamışlar mevzuyu:

![adim7][adim_7.png]

Burada soruyu çözen kişi `/dev/fd`'nin `/proc/self/fd`'ye symlink olduğunu ve `/dev/fd/../environ` -> `/proc/self/fd/../environ` -> `/proc/self/environ` olduğunu açıklıyorlar sağolsunlar.

Bu bilgileri kullanarak flagi elde edebiliriz.

![sonadim][son_adim.png]
