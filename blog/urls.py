"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



from article import views # burada article uygulaması içerisindeki viewsi al ve bunun içerisindeki indexide dahil et
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"), # burada path kısmında slash koyarsak django hata verecektir. Oyüzden şimdilik anasayfa için boş bırakıyoruz
    path('about/', views.about, name="about"), # bunu buraya tanımladıktan sonra views.py ye gidip about hakkında fonksiyon oluşturmamız gerekiyor
    path('articles/',include("article.urls")), # buradaki kodumuzun yaptığı işlem; articles dosyasına bak oradan articles.urls ye git. Article klasörünün içerisindeki urls.pyye gidiyoruz buradan
    path('user/',include("user.urls")),#user klasörün içerisindeki urls yi çekmek için böyle yapıyoruz
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
