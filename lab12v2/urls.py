"""lab12v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from giftReg.views import Registration, Home, Success, Users, Gifts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='Home1'),
    path('registration/', Registration.as_view(), name='Registration1'),
    path('success/', Success.as_view(), name='Success1'),
    path('users/', Users.as_view(), name='Users1'),
    path('gifts/', Gifts.as_view(), name='Gifts1')
]
