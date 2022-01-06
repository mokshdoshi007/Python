"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.indexPage, name="index"),
    path('register/', views.register, name="index"),
    path('fetch/', views.fetchall, name="fetch"),
    path('delete/',views.deleteprofile,name='delete'),
    path('update/',views.updateprofile,name='update'),
    path('login/',views.login,name='login'),
    path('profile/',views.getprofile,name='profile'),
    path('submitotp/',views.checkotp,name='submitotp'),
    path('forgotpassword/',views.forpass,name='forgotpassword'),
    path('verifyotp/',views.verifyotp,name='verifyotp'),
    path('editcity/',views.editcity,name='verifyotp'),
    path('changepassword/',views.changepass,name='changepassword'),
    path('logout/',views.logout,name='logout'),
    path('togglefav/',views.togglefav,name='togglefav'),
    path('rateturf/',views.rateturf,name='rateturf'),
    path('getfav/',views.getfav,name='getfav'),
    path('records/',views.records,name='records'),
]