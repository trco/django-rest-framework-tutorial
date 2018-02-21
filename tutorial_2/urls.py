from django.contrib import admin
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name = 'tutorial_2'
urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<pk>', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns) 
