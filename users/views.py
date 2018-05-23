from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_required(function):
    def wrapper(request, *args, **kw):
        user=request.user  
        if not (user.id and request.session.get('code_success')):
            return redirect('signup')
        else:
            return function(request, *args, **kw)
    return wrapper

# Create your views here.
def signup(request):
    return HttpResponse("hello")

@login_required
def groupA(request):
    return HttpResponse("groupA")

@login_required
def groupB(request):
    return HttpResponse("groupB")

@login_required
def index(request):
    return HttpResponse("index")