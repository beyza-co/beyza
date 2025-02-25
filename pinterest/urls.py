"""pinterest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path ,re_path , include
from django.views.static import serve
from user.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('register/',userRegister, name='register'),
    path('login/',userLogin,name='login'),
    path('logout/',userLogout, name='logout'),
    path('hesabım/',hesap,name='hesap'),
    path('pinadd/',pinAdd,name='pinAdd')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
