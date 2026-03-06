from django.shortcuts import render,redirect
from .models import Postathomepage
from .forms import createpostform
from django.contrib.auth.decorators import login_required

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