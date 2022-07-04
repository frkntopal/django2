from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm
 
from django.contrib import messages 

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
#authenticate : bu metodun amacı kullanıcı bilgilerine göre kullanıcı bilgilerinin veri kısmında olup olmadığını kontrol ediyor.
# Create your views here.

def register(request):
    #fonksiyonu tanımlamadan önce templates klasöründe register.html diye bir html oluşturmamız gerekiyor.
    form = RegisterForm(request.POST or None) #eğer post request değilse GET request oluşuyor çünkü None dedik. post request oluşmazsa anlarızki GET request oluşmuştur
    
    if form.is_valid(): #Post requestte clean metodunu çağırmak için is_valid() metodunu çağırmamız lazım. clean metodu da forms.pyde
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarıyla Kayıt Oldunuz...")

        return redirect("index")
    context = {
        "form" : form
    }
    return render(request,"register.html",context)

    
    
    
    """if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid(): #Post requestte clean metodunu çağırmak için is_valid() metodunu çağırmamız lazım. clean metodu da forms.pyde
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password) # set_passwordu kullanarak passwordumuzu şifrelemiş oluyoruz.

            newUser.save()
            login(request,newUser)

            return redirect("index")
        context = {
            "form" : form
        }
        return render(request,"register.html",context) # eğer fonksiyonumuz is_valid değilse bu sefer işlem buradan devam etmesi gerekiyor. şifreler eşit değilse tekrardan aynı sayfaya 
        #yönlendirior burası bizi.

    else:
        form = RegisterForm()
        context = {
            "form" : form
        }
        return render(request,"register.html",context)"""


def loginUser(request):
    #burada da aynı html sayfalarını oluşturmamız gerekiyor

    form = LoginForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalıdır...")
            return render(request,"login.html",context)
        
        messages.success(request,"Başarıyla Giriş Yaptınız...")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
        
def logoutUser(request):
    #burada da aynı html sayfalarını oluşturmamız gerekiyor
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")