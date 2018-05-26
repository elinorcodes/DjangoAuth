from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('company', views.CompanyView)
router.register('employee', views.EmployeeView)

urlpatterns = [
    path('', include(router.urls))
]