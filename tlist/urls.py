"""tlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from clists import views as cv
from users import views as uv
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cv.clist_landing_page, name='land_page'),
    path('clists/', include('clists.urls')),
    # Adding the urls for the allauth social login
    path('accounts/',include('allauth.urls')),
    # Adding the login and signup for the site with site credentials storage 
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/',uv.SignUpView.as_view(), name='signup'),
]
