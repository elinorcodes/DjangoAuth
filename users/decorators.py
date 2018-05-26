from django.shortcuts import render, redirect

# Custom decorators to handle user behaviour
# Custom login required decorator
def login_required(function):
    def wrapper(request, *args, **kw):
        user=request.user  
        if (user.id):
            return function(request, *args, **kw) 
        else:
            return redirect('users:home')
    return wrapper

#Custom logout_required decorator
def logout_required(function):
    def wrapper(request, *args, **kw):
        user=request.user  
        if not (user.id):
            return function(request, *args, **kw) 
        else:
            return redirect('users:index')
    return wrapper

# Custom login required decorator to access group A page
def login_required_groupA(function):
    def wrapper(request, *args, **kw):
        user=request.user  
        if (user.id and user.profile.group=='A'):
            return function(request, *args, **kw) 
        else:
            return redirect('users:index')
    return wrapper

#Custom logout required decorator to access group B page
def login_required_groupB(function):
    def wrapper(request, *args, **kw):
        user=request.user  
        if (user.id and user.profile.group=='B'):
            return function(request, *args, **kw) 
        else:
            return redirect('users:index')
    return wrapper
