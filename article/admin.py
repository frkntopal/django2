from django.contrib import admin

from .models import Article,Comment

# Register your models here.
admin.site.register(Comment) #Bizim modelimiz de  belli bir değişiklik olduğunda bunu django bildirmemiz gerekir. Migrations klasörünü değiştirmemiz gerekiyordu Bunu nasıl yapıyoruz peki;
#  terminnale py manage.py makemigrations şeklinde yazmamız gerekiyor, Sonrasında migrations klasörünün altında python dosyası oluşması gerekiyor. Oluştuktan sonra
# py manage.py migrate yazıyoruz. Sonrasında Admin paneline gidip comments oluşup oulşmadığına bak

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"] # burada da articlemizin sayfamızda hangi özellikler ile gözükeceğine karar veriyoruz
    list_display_links = ["title","created_date"] # bu modül ise oluşturma tarihi veya başlığa tıkladığımız zamanda article gitmemizi sağlayacak
    search_fields = ["title"] # burada aramaya başlık azarak makalemizi arayabiliriz
    list_filter = ["title"] # burada sayfamızn sağ tarafında son 7 günde yazılın son 1 ayda yazılan şeklinde filtreleme yapar
    class Meta:
        model = Article
#burada Article modelümüzü admin paneline ekliyoruz.