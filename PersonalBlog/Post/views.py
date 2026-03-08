from django.shortcuts import render,redirect
from .models import Postathomepage
from .forms import createpostform,signupform,loginform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.


def home(request):
    Postathomepageobj = Postathomepage.objects.all()
    return render(request,'homepage.html',{'Postathomepageobj':Postathomepageobj})

@login_required
def createpost(request):
    if request.method=='POST':
        createpostformobj= createpostform(request.POST,request.FILES)
        if createpostformobj.is_valid():
            post = createpostformobj.save()
            return redirect('homepage')
    else:
        createpostformobj= createpostform()

    return render(request,'createpost.html',{'createpostformobj':createpostformobj})


def signupview(request):
    if request.method=='POST':
        signupobj= signupform(request.POST)
        if signupobj.is_valid():
            post = signupobj.save()
            return redirect('homepage')
    else:
        signupobj= signupform()

    return render(request,'signup.html',{'signupobj':signupobj})

def loginview(request):
    if request.method == 'POST':
        loginobj = loginform(request,data=request.POST)
        if loginobj.is_valid():
            user = loginobj.get_user()
            login(request,user)
            return redirect('homepage')
    else:
        loginobj= loginform()    

    return render(request,'login.html',{'loginobj':loginobj})

def delete_post(request):
    return redirect('homepage')
