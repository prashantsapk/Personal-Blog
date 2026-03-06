from django.shortcuts import redirect
from django.http import request,response

def redirecttopost(request):
    return redirect('Post')