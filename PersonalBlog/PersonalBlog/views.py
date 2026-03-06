from django.shortcuts import redirect
from django.http import request,response

def redirecttopost(request):
    return redirect('http://127.0.0.1:8000/post/')