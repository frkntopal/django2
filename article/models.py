from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE,verbose_name="Yazar")#verbose_name auhotun sitede nasıl gözükmesini istersiniz şeklindeki komuttur.#modelscascade hangi kullanıcıdan bir veri silersek o kullanıcıyla alakalı her şey silenir
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank=True, null = True,verbose_name="Makaleye Fotoğraf Ekleyin") # Burada her makalemiz image olmak zorunda değil o yüzden burada blank = True null= True diyoruz. Yani bu alanlarımız hep blank hem null olarabilir diyoruz. 
    #bu modülü yazdıktan sonra py manage.py makemigrations yazdık terminale daha sonrasında da py manange.py migrate yazdık
    def __str__(self):
        return self.title # admin sayfasında makalemizi direk kimin yazdığı olarak görebiliriz self.author yazdığımızda
        #veya self.title ile makalemizin başlığıyla görebiliriz bunu çoğaltabiliriz 
       
    class Meta:
        ordering = ['-created_date'] # Bunun anlamı ise yazılan makaleni yayınlanan tarihe göre sıralamsına yarıyor.


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments") # burada ForeignKey yapmamızın sebebi oluşturduğumuz class'ı Article iletişim haline geçmesini sağlamak içindir.
#related_name'i yazmamızın sebebi; wğwe ben buraya comments dersem ileride bir tane article aldığın zaman article.comments dediğimizde aslında bunun comments tablosuna da erişebiliyoruz
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True) #bunları yazdıktan sonra admin.py ye gidiyoruz ve from.models import Article'ın yanına Comment'ti de ekliyoruz
    def __str__(self): # bunu yazmamızın sebebide admin panelinde yorumun direk ne olduğunu göstermek için. Aslında birnevi özelleştirdik.
        return self.comment_content
    
    class Meta:
        ordering = ['-comment_date'] #modelimizi değiştirdiğimiz için bunu djangoya söylememiz gerekiyor