CV PARSER PROJESİ

CV Parser; özgeçmiş veya CV olarak bilinen belgelerden, belirli bilgileri otomatik olarak çıkaran bir yazılım aracıdır. Bu projede, Python programlama dili kullanılarak e-posta, telefon ve ad soyad bilgilerini export eden bir CV Parser geliştirilmiştir. 1 Türkçe, 5 İngilizce CV için test edilmiştir. Bilgiler export edilirken Regex kullanılmıştır. Ancak ad soyad bilgilerini doğru export edebilmek için doğal dil işlemesi kullanılarak Nltk ve SpaCy kütüphanesi ile alternatif çözümler üretilmiştir. 

DOSYA: CVParser_Regex

ADIMLAR:
1. Kütüphanelerin İçe Aktarılması:
Re (düzenli ifadeler) ve PdfReader sınıfını içe aktarmak için PyPDF2 kütüphanesi kullanılır.

2. PDF Dosyasının Metne Dönüştürülmesi:
pdf_to_text(pdf_path) fonksiyonu, belirtilen PDF dosyasını okur.
PdfReader ile her sayfadaki metin çıkarılır ve birleştirilerek tek bir metin haline getirilir.

3. E-posta Adreslerinin Çıkarılması:
extract_emails(text) fonksiyonu, düzenli ifadeler (regex) kullanarak metin içindeki e-posta adreslerini tespit eder.
Bulunan e-posta adresleri bir liste olarak toplanır.

4. Telefon Numaralarının Çıkarılması:
extract_phone_numbers(text) fonksiyonu, farklı desenlere göre metin içindeki telefon numaralarını arar.
Desenlere uyan ilk telefon numarası bulunur ve döndürülür.
Desenler; boşluklarla ayrılmış, tirelerle ayrılmış, 11 haneli veya 10 haneli numaraları içerir.

5. İsimlerin Çıkarılması:
extract_names(text) fonksiyonu, düzenli ifadeler kullanarak metin içindeki isimleri tespit eder.
İsimler, baş harfleri büyük olan ve boşlukla ayrılan iki kelimeden oluşan örüntüye sahip metin parçalarıdır.

6. Ana Programın Çalıştırılması:
main() fonksiyonu, proje işlemlerini yürüten ana programdır.
Belirtilen PDF dosyasının yolu pdf_path değişkenine atanır.
PDF dosyası okunarak metne dönüştürülür.
E-posta adresleri, telefon numaraları ve isimler çıkarılır.
Elde edilen bilgiler ekrana yazdırılır.

7. Sonuçların Görüntülenmesi:
Çıkarılan e-posta adresleri, telefon numaraları ve ad soyadlar ayrı ayrı ekrana yazdırılır.

KULLANILAN KÜTÜPHANELER

Projede, metin işleme işlevleri için PyPDF2 ve düzenli ifadeler (regex) kullanılmıştır.
PyPDF2: PDF dosyalarını okuma ve metin çıkarma işlemleri için kullanılır.
Regex (Düzenli İfadeler): Metin içindeki e-posta adresleri, telefon numaraları ve isimleri tanımlamak için kullanılır.

FONKSİYONLAR
pdf_to_text(pdf_path): PDF dosyasını okur ve sayfa sayfa metin çıkarır.
extract_emails(text): Metin içindeki e-posta adreslerini düzenli ifadelerle tespit eder.
extract_phone_numbers(text): Metin içindeki telefon numaralarını farklı desenlere göre tespit eder.
extract_names(text): Metin içindeki isimleri tespit eder.

ANA PROGRAM

Ana program "main()" fonksiyonunda işlemler gerçekleştirilir.
Belirtilen PDF dosyası okunur ve metin haline getirilir.
Metin içinde e-posta adresleri, telefon numaraları ve ad soyadlar çıkarılır.

SONUÇLAR
Çıkarılan bilgiler ayrı ayrı listelenir ve ekrana yazdırılır.
E-posta adresleri, telefon numaraları ve ad-soyadlar örnek çıktılarda görülebilir.

ÇIKTILAR
Emails: örnek@gmail.com
Phone Number: 543-542-85-10
Names:
Industrial Engineering
Course Highlights
Data Management
Industrial Systems
Systems Thinking
Labor Law
...

GELİŞTİRME ÖNERİLERİ

1. Daha Kapsamlı İsim Algılama:
İsimleri tespit ederken daha kapsamlı bir yaklaşım kullanılabilir. Birden fazla kelimenin olduğu isimleri doğru bir şekilde tespit etmek için daha geniş bir isim örüntüsü kullanılabilir.
2. Doğal Dil İşleme (NLP) Kullanımı:
Doğal Dil İşleme tekniklerini (örneğin, Named Entity Recognition) kullanarak isimleri daha hassas bir şekilde tespit edilebilir.
3. Özel İsimlerin Tanımlanması:
Özel isimleri, sık kullanılan isimlerin listesine ekleyerek veya kullanıcının girdiği özel isimleri tanımlayarak doğruluğu arttırılabilir.
4. Yedek İsim Parçalarının İncelenmesi:
İsim tespiti yapılmazsa bile, metindeki büyük harfle başlayan kelime gruplarını incelenerek potansiyel ad-soyad adaylarını belirlenebilir.
5. Metin Ön İşleme İyileştirmeleri:
Metin ön işleme adımlarını geliştirerek, gürültüyü azaltabilir ve ad-soyad tespitini kolaylaştırılabilir.
6. Veri Etiketlemesi ve Eğitim Verisi Kullanımı:
Eğer yeterli veriye sahipseniz, isimleri ve diğer bilgileri elle etiketleyerek bir model eğitilebilir. Makine öğrenimi veya derin öğrenme yöntemleri kullanarak daha yüksek doğruluk elde edilebilir.
7. Topluluk Katılımı:
Proje açık kaynak olarak yayınlanarak topluluk katılımı teşvik edebilir ve farklı bakış açılarından gelen katkılar kullanılabilir.

DOSYA: CVParser_Nltk

NLTK KÜTÜPHANESİ

Natural Language Toolkit (NLTK), doğal dil işleme (NLP) alanında Python programcılarına yönelik bir kütüphanedir. NLTK, metin verileriyle çalışmayı kolaylaştıran çeşitli araçlar ve veri yapıları sunar. Bu kütüphane; metin madenciliği, metin analizi, metin önişleme, dil modelleri oluşturma ve daha birçok NLP görevini gerçekleştirmek için kullanılır.

nltk.tokenize.word_tokenize: Natural Language Toolkit (NLTK) kütüphanesinin word_tokenize fonksiyonu, metni kelimelere ayırmak için kullanılır. Metni cümlelerden ve kelimelerden oluşan bir liste olarak böler.

nltk.download('punkt'): NLTK kütüphanesinin punkt veri kümesini indirir. Bu veri kümesi, metinleri cümlelere ve kelimelere ayırmak için kullanılan önişleme araçlarını içerir.

Metin işleme ve basit kurallara dayalı bir yöntem (metni ayırma, büyük harfle başlayan kelimeleri seçme, kombinasyonları oluşturma ve sayma) kullanarak ad-soyad kombinasyonları tespit etmeye çalışılabilir. Belirli koşullara göre filtrelenerek ad soyad kombinasyonları olarak çıkarılır.

Denenen örneklerde ad soyad çıktısı elde edildi. Ancak bununla birlikte farklı kombinasyonlar da bulundu. Farklı cv samplelarında programın ilk ad soyad çıktısının doğru sonuç verdiği gözlemlendi. Dolayısıyla kod, sadece ilk çıktısı olan ad soyad kombinasyonunu vermesi şeklinde düzenlenerek ilk kombinasyonu bulduktan sonra döngü sonlandırıldı.

ÇIKTILAR
First Full Name Found:
ESRA AKILLI

DOSYA: CVParser_SpaCy

SpaCy KÜTÜPHANESİ

SpaCy; hızlı, verimli ve kolay kullanılabilir bir şekilde metinlerin analizi, dil yapıları ve anlamsal içeriklerin çıkarılması gibi NLP görevlerini gerçekleştirmek için tasarlanan Python kütüphanesidir.  tr_core_news_sm ve xx_ent_wiki_sm modelleri, SpaCy'nin farklı özelliklere sahip önceden eğitilmiş modelleridir ve farklı amaçlar için kullanılırlar.

tr_core_news_sm:
Amaç: Temel doğal dil işleme görevlerini gerçekleştirmek üzere eğitilmiş bir Türkçe modelidir.
Kapsam: Cümle ayrıştırma (parsing), kelime ayrıştırma (tokenization), cümle sınıflandırma (sentence classification), kelime vektörleri (word vectors), kelimelem (lemmatization), ve cümlenin dillemi (part-of-speech tagging) gibi temel görevleri destekler.
Varsayılan Entite Etiketleri: Türkçe dilinde ad-soyad, organizasyon, tarih gibi temel varlıkların etiketlenmesi için kısıtlı bir destek sağlar.

xx_ent_wiki_sm:
Amaç: Çoklu dilde (multilingual) adlar ve varlıklar (entities) tanımak için eğitilmiş bir modeldir.
Kapsam: Çoklu dili destekler ve temel doğal dil işleme görevlerine ek olarak ad ve varlık tanıma konusunda daha geniş bir destek sunar.
Varsayılan Entite Etiketleri: Farklı dillerdeki metindeki adlar, organizasyonlar, tarihler, para birimleri, yüzlerce farklı varlık türünün etiketlenmesi için daha geniş bir destek sunar.

Türkçe metinlerdeki "PERSON" (kişi) etiketlerini ad ve soyad olarak kabul eder. Bu yöntem daha karmaşık isim analizi için daha iyi sonuçlar verebilir. Öncelikle sadece Türkçe metinlerde ad-soyad ikililerini bulmak için tr_core_news_sm modeli denendi. Hata alınarak kaynağı Anaconda sanal ortamı olabileceğinden öncelikle terminalden kütüphane kurulumu silinip tekrar yüklendi. Tekrar aynı hata alınınca hata sürüm değişikliklerinden kaynaklanabileceği için tr_core_news_sm modeline geçildi. Eski bir sürüm olan SpaCy'nin 3.0.6 sürümü ile tr_core_news_sm modeli indirilerek çözüldü.

Ancak bu sefer de sadece "Full Names:" çıktısı alındı. Yani metin içindeki kişi isimleri doğru bir şekilde tespit edilemedi. Modelin sonuçlarını daha ayrıntılı incelemek için her bir varlık (entity) ve etiketi yazdırılarak hangi türdeki varlıkların tespit edildiği gözlemlendi.

ÇIKTILAR
ESRA AKILLI       
OBJECTIVE  
EDUCATION ORG
Istanbul LOC
Turkey LOC
...
