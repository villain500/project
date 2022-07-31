import re
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from adminsite.models import Slider
from products.models import Football
from products.models import Jersey
from products.models import Shoe
from products.models import GP_Glub
from products.models import Other
def index(request):
    # slider section
    slider=Slider.objects.all()
    
    # sending email
    if request.method=="POST":
        email=request.POST['email'] 
        message=request.POST['message'] 
        send_mail(
            email,
            message,
            'contactu07@gmail.com',
            ['siyammaahmud@gmail.com'],
            fail_silently=False,
        )

    
    return render(request,'index.html',{'slider':slider})

def products(request):
    football=Football.objects.all()
    jersey=Jersey.objects.all()
    shoe=Shoe.objects.all()
    glubs=GP_Glub.objects.all()
    other=Other.objects.all()
    data={
        'football':football,
        'jersey':jersey,
        'shoe':shoe,
        'glubs':glubs,
        'other':other,
    }
    return render(request,'Products.html',data)

def about(request):
    return render(request,'about.html')

def term_con(request):
    return render(request,'term & Con.html')

def siteUsers(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        confirm_pass=request.POST['confirm_pass']

        if password != confirm_pass:
            return HttpResponse("password didn't matched")

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        return HttpResponse('thanks for creating account </br><a href="/">Return Home</a>')
    return render(request,'signup.html')

def logiin(request):
    if request.method=="POST":
        loguname=request.POST['loguname']
        logpass=request.POST['logpass']

        user = authenticate(username=loguname,password=logpass)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponse('Log in successfull</br><a href="/">Return Home</a>')
    return render(request,'login.html')

def log_out(request):
    logout(request)
    return HttpResponse('''log out successfull </br><a href="/">Return Home</a>''')

