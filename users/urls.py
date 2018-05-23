from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('logout', views.logoutUser, name='logout'),
    path('groupA', views.groupA, name='groupA'),
    path('groupB', views.groupB, name='groupB'),
    path('', views.index, name='index')
]
