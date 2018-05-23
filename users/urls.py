from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('groupA', views.groupA, name='groupA'),
    path('groupB', views.groupB, name='groupB'),
    path('index', views.index, name='index')
]
