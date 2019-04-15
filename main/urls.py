from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('formular/', views.formular, name="formular"),
    path('formular_submit/', views.formular_submit, name="formular_submit"),
]
