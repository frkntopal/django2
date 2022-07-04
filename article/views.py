from email import message
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
import article
#get_object_or_404'ün yaptığı iş şudur; mesela article/40 a gittin. Eğer 40 numaralı makale varsa bu makaleyi gösteriyor fakat 40 numaralı makale yoksa direk 404 found hatası veriyor
from article.models import Article
from .forms import ArticleForm
from .models import Article,Comment 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required # login_reqıired'ın amacı eğer biz siteye giriş yapmadıysak articlelara erişemiyoruz. Makaleleri görebilmek için illaki giriş yapmımız şart.
# Create your views here.

def articles(request):

    keyword = request.GET.get("keyword") # if keywordda dahil burada yaptığımız olay arama çubuğuna işlem kazandırmak. 
    #if koşulunu pek anlamadım eğer gerekirse 234.videoyu izle

    if keyword:
        articles = Article.objects.filter (title__contains = keyword)

        return render(request,"articles.html",{"articles":articles})
        
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})



#urls.py ye eklediğimiz pathlerin fonksiyonlarını views.pyye yazıyoruz

def index (request): # requesti araştır,bilmiyorsun.
    #return HttpResponse("Anasayfa")
    #şimdi buradaki durum biraz özel, Eğer biz dökümanımıza ayriyetten ek olarak bir veri yollamak istiyorsak bunu 
    #context adı altında yapıyoruz. Örnek olarak ; context = {"number1":20,"number2":40} sonra bunu gidip index.htmlde 
    #tanımlamımız gerekiyor. Orada da blockların içerisinde <p> altında {{number1}} şeklinde tanımlıyoruz.(209.video)
    # context = {
    #     "number1":[1,2,3,4,5,6],
    # } daha sonra index fonksiyonun için return render(request,"index.html",context) şeklinde yazmamız gerekiyor
    return render(request,"index.html",)

def about (request):
    return render (request,"about.html")
@login_required(login_url="user:login") # bunu yazarak login_required'i aktif etmiş oluyoruz

def dashboard(request):
    articles = Article.objects.filter(author = request.user) #Article tablosundan biz sadece giriş yapmış kullanıcıların makalelerini almak istiyoruz. O yüzden object.filter ' ı kullanıyoruz
    context = {
        "articles": articles
    }
    return render (request,"dashboard.html",context)

@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():

        article = form.save(commit=False)

        article.author = request.user
        article.save()

        # şimdi burada önemli bir konu var. Eğer sadece form.save() yazarsak sadece bizim makalemizi kayıt ediyor.
        #fakar author bilgimizi kaydetmediği için hata vermiş oluyor. Burada önemli olan nokta user bilgisinide vermemiz gerekiyor
        #o yüzden article = form.save(commit=False)  yaparak article.author = request user yapıyoruz burada user yani yazar bilgiside gelmiş olucak
        #sonra hem makaleyi hem yazarı kaydetmek için article.save() yapıyoruz

        messages.success(request,"Makale başarıyla oluşturuldu.")
        return redirect("article:dashboard")

    return render (request,"addarticle.html",{"form":form})

def detail(request,id):
    # article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)

    comments = article.comments.all() # şimdi burada articleların içindeki commentleri çekmemiz için models.py comment sınıfın altında related_name="comments" olması gerekiyordu. 
    #Bunu değiştirirsek eğer oradaki related_name ne ise onu buraya yazarak article 'lardaki commentleri alabiliriz
    return render(request,"detail.html",{"article":article,"comments":comments})

@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None, instance= article)
    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla güncellendi.")
        return redirect("article:dashboard")
    
    return render (request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)

    article.delete()

    messages.success(request,"Makale Başarıyla Silindi")

    return redirect ("article:dashboard")

def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content") # bunları yazdıktan sonra views.py ye Comment modülünü import etmemiz gerekiyor.

        newComment = Comment (comment_author = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    
    return redirect(reverse("article:detail",kwargs = {"id":id})) # burada reverse aslında şu açıklamyı daha basit hale çevirdi; /articles/detail/15
    #burada reverse kullanmadan önce import etmemiz gerekiyor. reverse kullanımını internetten araştır önemli.



















#Terminalden user ve article oluşturma

# py manage.py shell

#Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from django.contrib.auth.models import User
# >>> from article.models import Article
# >>> User
# <class 'django.contrib.auth.models.User'>
# >>> newUser = User(username = "denemekullanici", password= "1234")
# >>> newUser.save()
# >>> newUser2 = User ( username = "denemekullanici2")
# >>> newUser2.set_password("1234")
# >>> newUser2.save()
# >>> newUser3.save()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'newUser3' is not defined
# >>> newUser3 = User()
# >>> newUser3.username = "denemekullanici3"
# >>> newUser3.set_password = "1234"
# >>> newUser3.save()
# >>> article = Article(title = "Dhango Shell Deneme",content = "İçeri içerik",author = newUser3)
# >>> article.save()
# >>> Article.objects.create(title = "deneme 21", content = "21"author = newUser2)
#   File "<console>", line 1
#     Article.objects.create(title = "deneme 21", content = "21"author = newUser2)
#                                                           ^^^^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# >>> Article.objects.create(title = "deneme 21", content = "21",author = newUser2) 
# <Article: deneme 21>
# >>>
