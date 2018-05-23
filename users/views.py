from django.contrib.auth  import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import SignUpForm
from .decorators import login_required, login_required_groupA, login_required_groupB, logout_required

# View functions

@logout_required
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.group = form.cleaned_data.get('group')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            print("error")
    form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required_groupA
def groupA(request):
    return render(request, 'users/groupA.html')

@login_required_groupB
def groupB(request):
    return render(request, 'users/groupB.html')

@login_required
def index(request):
    if request.user.profile.group=='A':
        return redirect('groupA')
    elif request.user.profile.group=='B':
        return redirect('groupB')
    else:
        return HttpResponse("hello there!")

@login_required
def logoutUser(request):
    logout(request)
    return redirect('signup')