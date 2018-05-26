from django.contrib.auth  import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

from .forms import SignUpForm, SignInForm
from .decorators import login_required, login_required_groupA, login_required_groupB, logout_required

# View functions

@logout_required
def home(request):
    return render(request, 'users/home.html')

@logout_required
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            user.refresh_from_db()
            user.profile.group = form.cleaned_data.get('group')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('users:index')
        else:
            print("error")
    form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

@logout_required
def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            find_user = User.objects.get(username=request.POST['username'])
            user = authenticate(username=find_user.username, password=request.POST['password'])
            login(request, user)
            return redirect('users:index')
        else:
            print("error")
    form = SignInForm()
    return render(request, 'users/signin.html', {'form': form})

@login_required_groupA
def groupA(request):
    return render(request, 'users/groupA.html')

@login_required_groupB
def groupB(request):
    return render(request, 'users/groupB.html')

@login_required
def index(request):
    if request.user.profile.group=='A' or request.user.is_staff==True:
        return redirect('users:groupA')
    return redirect('users:groupB')

@login_required
def logoutUser(request):
    logout(request)
    return redirect('users:home')