from django.contrib import admin
from django.urls import path

from . import views


app_name = 'snippets'
urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<pk>', views.snippet_detail),
]
