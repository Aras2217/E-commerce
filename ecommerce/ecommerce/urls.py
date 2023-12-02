"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf.urls.static import static
from myApp.views import *
from appUser.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage, name="indexPage"),
    path('contact/', contactPage, name="contactPage"),
    path('shop/', shopPage, name="shopPage"),
    path('detail/<slug>/', detailPage, name="detailPage1"),
    path('detail/<slug:slug>/color/<slug:color>', detailPage, name="detailPage2"),
    path('basketShop/', basketShop, name="basketShop"),
    path('about/', aboutPage, name="aboutPage"),
    
    
    # === USER ===
    path('login/', loginUser, name="loginUser"),
    path('logout/', logoutUser, name="logoutUser"),
    path('register/', registerUser, name="registerUser"),
    path('myaccount/', accountPage, name="accountPage"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
