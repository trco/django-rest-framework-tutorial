"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('tutorial_1/', include('tutorial_1.urls', namespace='tutorial_1')),
    path('tutorial_2/', include('tutorial_2.urls', namespace='tutorial_2')),
    path('tutorial_3/', include('tutorial_3.urls', namespace='tutorial_3')),
    path('tutorial_4/', include('tutorial_4.urls', namespace='tutorial_4')),
    path('tutorial_5/', include('tutorial_5.urls')),
    path('tutorial_6/', include('tutorial_6.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
