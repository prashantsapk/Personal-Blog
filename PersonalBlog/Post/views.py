from django.shortcuts import render,redirect
from .models import Postathomepage,commentofpost
from .forms import createpostform,signupform,loginform,commentform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your views here.


@login_required
def home(request):
    Postathomepageobj = Postathomepage.objects.all()
    return render(request,'homepage.html',{'Postathomepageobj':Postathomepageobj})

@login_required
def createpost(request):
    if request.method=='POST':
        createpostformobj= createpostform(request.POST,request.FILES)
        if createpostformobj.is_valid():
            post = createpostformobj.save(commit=False)
            post.user=request.user
            post.save()
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

@login_required
def delete_post(request):
   
    if request.method=="POST":
        id=request.POST.get('id')
        post= Postathomepage.objects.get(id=id)
        post.delete()
        return redirect('homepage')



@login_required
def update_post(request,id):
   
    
    if request.method=='POST':
        post= Postathomepage.objects.get(id=id)
        updatepostobj = createpostform(request.POST,instance=post)
        updatepostobj.save()

        return redirect('homepage')

    else:
        post= Postathomepage.objects.get(id=id)
        updatepostobj = createpostform(instance=post)

    
    return render(request,'editpost.html',{'updatepostobj':updatepostobj})
  
@login_required
def commentview(request,id):

    if request.method=='POST':
        newform = commentform(request.POST)
        if newform.is_valid():
            commentobj = newform.save(commit=False)
            post = Postathomepage.objects.get(id=id)
            commentobj.post = post
            commentobj.user = request.user 
            commentobj.save()
        

       

    else:
        post = Postathomepage.objects.get(id=id)
        commentobj=post.comments.all()
        form = commentform()
        return render(request,'comment.html',{'commentobj':commentobj,'form':form})

    return redirect('homepage')


@login_required
def profileview(request,id):
    obj = User.objects.get(id=id)
    profileobj = obj.posts.all()
    return render(request,'profilepage.html',{'profileobj':profileobj,'obj':obj})


