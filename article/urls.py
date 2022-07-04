from django.contrib import admin
from django.urls import path
from . import views


app_name = "article"

urlpatterns = [
    path('create/',views.index,name="index"),# blog içerisindenki urls.py den buraya gelip create yapıyoruz. views i import ettikten sonra views.index yapıyoruz. İndexi daha önceden boş slash olarak tanımladığımızdan direk anasayfaya yönlendiriyor bizi bu urls
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addarticle/',views.addArticle,name="addarticle"),
    path('article/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.updateArticle,name="update"),
    path('delete/<int:id>',views.deleteArticle,name="delete"),
    path('',views.articles,name="articles"),
    path('comment/<int:id>',views.addComment,name="comment"), #eğer views.--- buraya yazdığımız fonksiyon adı views.py dosyasında yoksa
    #views.py dosyasına gidip orada yazdığımız fonksiyonun fonkiyonunu yazmamız gerekiyor
   
    ]
