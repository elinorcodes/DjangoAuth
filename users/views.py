from django.contrib.auth  import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import HttpResponse

# Custom decorators to handle user behaviour
# Custom login required decorator
def login_required(function):
    def wrapper(request, *args, **kw):
        user=request.user  
        if not (user.id and request.session.get('code_success')):
            return redirect('signup')
        else:
            return function(request, *args, **kw)
    return wrapper

# View functions

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.group = form.cleaned_data.get('group')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required
def groupA(request):
    return HttpResponse("groupA")

@login_required
def groupB(request):
    return HttpResponse("groupB")

@login_required
def index(request):
    return HttpResponse("index")