"""
URL configuration for goprosperous project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('register/', register),
    path('forgot_password/', forgot_password),
    path('change_password/', change_password),
    path('otp/', otp),
    path('', dashboard),
    path('profile/', profile),
    path('upgrade_plan/', upgrade_plan),
    path('lookalike_finder/', lookalike_finder),
    path('lookalike_finder_sidebar/', lookalike_finder_sidebar),
    path('search/', search),
    path('search_company/', search_company),
    path('search_person/', search_person),
    path('company_profile/', company_profile),
    path('person_profile/', person_profile),
    path('list/', list),
    path('export_log/', export_log),
    path('saved_search/', saved_search),
    path('email_personalization/', email_personalization),
]